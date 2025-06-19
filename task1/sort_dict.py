# sort_dict.py
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

# Test data
data = [
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Test function
sorted_data = sort_dict_list_manual(data, "age")
print("Manual Sort:", sorted_data)