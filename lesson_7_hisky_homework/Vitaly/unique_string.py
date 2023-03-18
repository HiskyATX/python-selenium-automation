def unique_chars_string(my_string):
    char_set = set(my_string)			    # Create a set of characters in the string
    return len(char_set) == len(my_string)	# Comparing the length of the set to the length of the original string.
                                            # If they're equal, all characters are unique


user_input = (input("Enter a string with more than 2 unique characters and press enter: \n"))    #asking from input from the user prompt


print(unique_chars_string(user_input))  # Output: boolean