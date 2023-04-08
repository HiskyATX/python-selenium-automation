def descending_insertion_sort (test_list):

    for i in range(1, len(test_list)):      # Iterating through the list, starting from the second element
        key = test_list[i]                  # Storing the current element as the key
        j = i - 1                           # Setting the variable j as the previous element's index

        while j >= 0 and test_list[j] < key:    # Looping backwards through the list, from index j to the beginning.
                                                # Checking if the current element is less than the key.
            test_list[j + 1] = test_list[j]
            j -= 1                          # If it is, shifting the current element one position to the right
        test_list[j + 1] = key              # After shifting all smaller elements to the right, inserting the key in the correct position

    return test_list                        # Returning the sorted list in descending order


test_list = [729, 46, 27, 23, 0, -9]
sorted_list = descending_insertion_sort(test_list)
print(sorted_list)
