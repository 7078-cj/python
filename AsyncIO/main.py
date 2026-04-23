import asyncio
import time

def synchronous_function(str):
    print("This is a synchronous function.")

    time.sleep(1)
    print("Synchronous function completed.")
    return f'Hello, {str}!(Synchronous)'

async def async_function(str):
    print("This is an asynchronous function.")
    
    await asyncio.sleep(1)
    print("Async function completed.")
    return f'Hello, {str}!(Asynchronous)'

async def main():
    #coroutine
    coroutine_obj = async_function("AsyncIO")
    print(coroutine_obj)
    
    coroutine_result = await coroutine_obj
    print(coroutine_result)
    
    #task
    task = asyncio.create_task(async_function("AsyncIO"))
    print(task)
    
    task_result = await task
    print(task_result)

if __name__ == "__main__":

    asyncio.run(main())