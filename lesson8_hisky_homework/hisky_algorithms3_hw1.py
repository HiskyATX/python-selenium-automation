#Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]


def numbers_below_arithmetic_mean(sample):
    mean = sum(sample) / len(sample) # using the sum and len functions to calculate the mean
    results = [] # creating an empty list to fill with numbers below the mean

    for i in sample:    ##Iterating through each number of the list
        if i < mean:
            results.append(i)    ##If the number is less than the mean, appending it to the results

    return results


test_numbers = [1, 3, 5, 6, 4, 10, 2, 3]
results = numbers_below_arithmetic_mean(test_numbers)
print('The numbers below the arithmetic mean are:')
print(results)


