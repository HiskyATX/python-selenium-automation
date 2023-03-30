# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_number(digits):
# starting from the least significant digit
    i = len(digits) - 1
#if encountering 9, setting it to 0 and move on to the next digit
    while i >= 0 and digits[i] == 9:
        digits[i] = 0
        i -= 1
# if reached the leftmost digit, and it is 9, add a 1 at the beginning
        if i < 0:
            digits.insert(0, 1)
#otherwise, incrementing the current digit by 1.
        else:
            digits[i] += 1
#returning the updated list of digits.
    return digits


test_list = [1, 2, 9]
output_list = increment_number(test_list)
print(test_list) # [1, 3, 0]
