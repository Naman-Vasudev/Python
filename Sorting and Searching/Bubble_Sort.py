def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0, n-1):
        # for round 1 to n-1
        swapped = False
        
        for j in range(0, n-i-1):
            # process elements till n-i th index
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Python swap
                swapped = True
        
        if not swapped:
            # already sorted
            break
    return arr  # Fixed indentation - return outside the loop


unsorted_list = list(map(int, input("Enter the elements of the list: ").split()))
print(bubble_sort(unsorted_list))