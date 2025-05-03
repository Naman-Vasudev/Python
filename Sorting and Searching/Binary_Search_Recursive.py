def binary_search_recursive(arr, start, end, key):
    # Base condition: if start index exceeds end index, key is not present
    if end >= start:
        mid = (start + end) // 2  # Calculate the mid index

        # If the key is found at mid
        if arr[mid] == key:
            return mid
        
        # If key is smaller than mid element, search in the left subarray
        elif arr[mid] > key:
            return binary_search_recursive(arr, start, mid - 1, key)
        
        # Else search in the right subarray
        else:
            return binary_search_recursive(arr, mid + 1, end, key)
    
    # If element is not found
    return -1


arr = list(map(int, input("Enter a sorted list (space-separated): ").split()))
print(f"Your sorted list: {arr}")

# Key to search
key = int(input("Enter the number you wish to search: "))

# ------------------- Output Section -------------------
index = binary_search_recursive(arr,0,(len(arr)-1),key)
if index != -1:
    print(f"The element {key} is found at index {index}.")
else:
    print(f"The element {key} is not found in the list.")
