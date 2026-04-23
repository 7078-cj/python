import time
import asyncio

#this is bad practice because it blocks the event loop,
# preventing other tasks from running concurrently.
# In a real-world application, 
# you should use non-blocking calls like asyncio.sleep() 
# instead of time.sleep() to avoid blocking the event loop.

#you should use asynchronous functions to take advantage of the 
# benefits of asyncio, and avoid blocking the event loop 
# with synchronous calls like time.sleep().

async def fetch_data(param, delay):
    print(f"Fetching data for {param}...")
    time.sleep(delay) 
    print(f"Data fetched for {param}.")
    time_taken = time.perf_counter()
    return f"Data for {param}: {time_taken} seconds."

async def main():
    task1 = asyncio.create_task(fetch_data("Parameter 1", 2))
    task2 = asyncio.create_task(fetch_data("Parameter 2", 1))

    result1 = await task1
    print('result1 complete')

    result2 = await task2
    print('result2 complete')
    return [result1, result2]
    
t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1} seconds.") 