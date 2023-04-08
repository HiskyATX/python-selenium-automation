def descending_selection_sort(test_list):
    n = len(test_list)                      #creating a variable to store the list length
    for i in range(n):
        max_element = test_list[i]          # initializing maximum element
        max_index = i                       # initializing index as the first element
        for j in range(i+1, n):             # finding the maximum element
            if test_list[j] > max_element:  # comparing the current element (test_list[j]) with the current maximum element.
                                            # if the current element is greater than the maximum element
                max_element = test_list[j]
                max_index = j               # updating max_element and max_index with the current element and its index.
        test_list[i], test_list[max_index] = test_list[max_index], test_list[i] # Swapping the found maximum element with the first element

    return test_list


test_list = [27, 729, 46, -9, 23, 0]
print(descending_selection_sort(test_list))
