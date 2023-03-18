def string_swapping(my_string):
# Find the midpoint of the given string
    midpoint = len(my_string) // 2


# If the string has odd number of characters, increase the first half of it by one index
    if len(my_string) % 2 != 0:
        midpoint += 1


# Split the string into two halves
    first_half = my_string[:midpoint]
    second_half = my_string[midpoint:]


# Swap the two halves and return the two strings concatenated
    return second_half + first_half


#asking from input from the user prompt
user_string = (input("Enter a string with more than 2 characters and press enter: \n"))


swapped_string = string_swapping(user_string)
#
print('The string you entered looks like this when swapped:',(swapped_string))