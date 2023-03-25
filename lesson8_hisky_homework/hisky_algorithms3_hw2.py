#Two Lowest Elements
#When given a list of elements, find the two lowest elements. #They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


# Taking a list as input.
def find_two_smallest_numbers(number_list):
# initializing lowest1 and lowest2 as the first two numbers of the list.
    smallest1 = number_list[0]
    smallest2 = number_list[1]

# iterating over the remaining numbers of the list using a for loop that checks if it is lower than lowest1.
# If it is, lowest1 becomes that element and lowest2 becomes the previous value of lowest1.
    for i in number_list[2:]:
        if i < smallest1:
            smallest2 = smallest1
            smallest1 = i
# If the element is not lower than lowest1 but is lower than lowest2, lowest2 becomes that element.
        elif i < smallest2:
            smallest2 = i
# Return the two lowest numbers
    return smallest1, smallest2


test_list = [198, 3, 4, 9, 10, 9, 2]
results = find_two_smallest_numbers(test_list)
print("The lowest numbers of the list are:")
print(results)