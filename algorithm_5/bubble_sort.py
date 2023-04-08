def descending_bubble_sort(array):
    n = len(array)                          #creating a variable to store the list length
    for i in range(n):
        swapped = False                     # Setting a flag for checking if any swap is made in the current pass
        for j in range(0, n-i-1):
            if array[j] < array[j+1]:       # Comparing consecutive elements and swapping them if they are in the wrong order
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:                      # If no swaps are made in the current pass, then the array is already sorted
            break                            # breaking the loop

    return array                             # Returning the sorted array in descending order


test_array = [27, 729, 46, -9, 23, 0]
print(descending_bubble_sort(test_array))

