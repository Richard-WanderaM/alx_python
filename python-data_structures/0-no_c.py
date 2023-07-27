def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

# new_string = "": Initialize an empty string to hold the characters that are not 'c' or 'C'.

# for char in my_string: Iterate through each character of the input string.

# if char.lower() != 'c':: Check if the lowercase version of the current character is not 'c'. The lower() method is used to handle both 'c' and 'C' cases.

# new_string += char: If the character is not 'c' or 'C', add it to the new_string.

# return new_string: Return the new_string, which contains the input string with all 'c' and 'C' characters removed.