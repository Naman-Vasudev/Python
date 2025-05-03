def binary_search(sorted_list, key):
    start = 0
    end = len(sorted_list) - 1
    
    while start <= end:
        # Mid-point calculation (avoids overflow for very large values)
        mid = start + (end - start) // 2

        if sorted_list[mid] == key:
            return mid  # Key found at index mid
        elif sorted_list[mid] > key:
            end = mid - 1  # Search in the left half
        else:
            start = mid + 1  # Search in the right half

    return -1  # Key not found

# ------------------- Input Section -------------------
# User inputs a sorted list (monotonically increasing)
sorted_list = list(map(int, input("Enter a sorted list (space-separated): ").split()))
print(f"Your sorted list: {sorted_list}")

# Key to search
key = int(input("Enter the number you wish to search: "))

# ------------------- Output Section -------------------
index = binary_search(sorted_list, key)
if index != -1:
    print(f"The element {key} is found at index {index}.")
else:
    print(f"The element {key} is not found in the list.")