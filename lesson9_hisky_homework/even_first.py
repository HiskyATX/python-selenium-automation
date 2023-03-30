# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(numbers):
    i = 0                           #pointing to the beginning of the list
    j = len(numbers)-1              #pointing to the end of the list
    while i < j:                    #looping thru the list
        if numbers[i] % 2 == 0:     #verifying if number is even
            i += 1                  #if it is, incrementing i
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i] # swapping elements if the element at i is odd and the element at j is even.
            j -= 1                              #decrementing j

    return numbers


testing_list = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(testing_list))
