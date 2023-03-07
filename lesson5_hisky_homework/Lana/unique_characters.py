# 5*[Not required]. Solve Amazon interview question:
# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
####################################################################################################

def find_unique_character(my_string):
    my_string = my_string.lower()  # converting to lowercase so it's not case-sensitive

    for char in my_string:
        count = my_string.count(char)  # counting number of characters in the string
        if count == 1:          # if the number of characters in the string equals 1
            return char         #returning character as function result

    return ''                   #returning empty string if more than one occurrance is found


user_string = input('Enter a word and hit enter: \n')

unique_character = find_unique_character(user_string)
if len(unique_character)!=1:
    print('No unique character was found')
else:
    print('The unique character is:', unique_character)