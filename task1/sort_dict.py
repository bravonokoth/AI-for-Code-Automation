# sort_dict.py
import time

# Manual Implementation
def sort_dict_list_manual(data, key):
    """
    Sort a list of dictionaries by a specified key.
    Args:
        data (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x[key])

# Copilot-Suggested Implementation
def sort_dict_list_copilot(data, key):
    """
    Sort a list of dictionaries by a given key.
    Args:
        data (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        return sorted(data, key=lambda x: x[key], reverse=False)
    except KeyError:
        print(f"Key '{key}' not found in one or more dictionaries.")
        return data

# Test data
data = [
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Test functions
sorted_data_manual = sort_dict_list_manual(data, "age")
print("Manual Sort:", sorted_data_manual)

sorted_data_copilot = sort_dict_list_copilot(data, "age")
print("Copilot Sort:", sorted_data_copilot)

# Benchmark both functions
def benchmark(func, data, key, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        func(data.copy(), key)
    return time.time() - start

# Run benchmarks
manual_time = benchmark(sort_dict_list_manual, data, "age")
copilot_time = benchmark(sort_dict_list_copilot, data, "age")

print(f"Manual Time: {manual_time:.4f}s")
print(f"Copilot Time: {copilot_time:.4f}s")