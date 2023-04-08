def merge_sort(test_array):
    if len(test_array) <= 1:   #if the array has only one element or is empty, it is already sorted
        return test_array
    mid = len(test_array) // 2     #    # splitting the array into two halves
    left_half = test_array[:mid]   # left half is a slice from the beginning to the middle of the array
    right_half = test_array[mid:]  # right half is a slice from the middle to the end

    sorted_left_half = merge_sort(left_half)    #  recursively sorting the left half
    sorted_right_half = merge_sort(right_half)  #  recursively sorting the right half

    return merge(sorted_left_half, sorted_right_half)   # merging the two sorted halves

def merge(left, right):
    merged_arr = []  # initializing the merged array
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):  # iterating through the left and right arrays
        if left[left_index] > right[right_index]:       # comparing their elements
            merged_arr.append(left[left_index])         # adding the larger one to the merged array

            left_index += 1
        else:
            merged_arr.append(right[right_index])
            right_index += 1

    while left_index < len(left):       #  if there are any remaining elements in the left array
        merged_arr.append(left[left_index])     # adding them to the merged array
        left_index += 1                         # and incrementing left index

    while right_index < len(right):     # If there are any remaining elements in the right array
        merged_arr.append(right[right_index])   # add them to the merged array
        right_index += 1                        # and incrementing right index

    return merged_arr


test_array = [27, 0, 729, 46, -9, 23]

# Sort the input array in descending order using merge sort
sorted_arr = merge_sort(test_array)

print("Input array: ", test_array)
print("Sorted array in descending order: ", sorted_arr)


