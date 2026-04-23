import time

def fetch_data(param):
    print(f"Fetching data for {param}...")
    time.sleep(2)  
    print(f"Data fetched for {param}.")
    time_taken = time.perf_counter()
    return f"Data for {param}: {time_taken} seconds."

def main():
    result1 = fetch_data("Parameter 1")
    print(result1)

    result2 = fetch_data("Parameter 2")
    print(result2)
    
t1 = time.perf_counter()

results = main()
print(results)
t2 = time.perf_counter()
print(f"Total time taken: {t2 - t1} seconds.")