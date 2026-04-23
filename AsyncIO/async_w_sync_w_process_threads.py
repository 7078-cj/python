import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

def fetch_data(param, delay):
    print(f"Fetching data for {param}...")
    time.sleep(delay)
    print(f"Data fetched for {param}.")
    time_taken = time.perf_counter()
    return f"Data for {param}: {time_taken} seconds."

async def main():
    # THREADS (I/O simulation)
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, "Parameter 1", 2))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, "Parameter 2", 1))

    result1 = await task1
    print('result1 complete')

    result2 = await task2
    print('result2 complete')

    # PROCESSES (CPU-bound simulation)
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        task1 = loop.run_in_executor(pool, fetch_data, "Parameter 1", 2)
        task2 = loop.run_in_executor(pool, fetch_data, "Parameter 2", 1)

        result1 = await task1
        print('result1 complete')

        result2 = await task2
        print('result2 complete')

    return [result1, result2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Total time taken: {t2 - t1} seconds.")