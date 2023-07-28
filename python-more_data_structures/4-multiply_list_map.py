def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

# We se the map function to achieve the desired behavior.
# The map function applies a given function to each item of an iterable,
# (e.g., list) and returns an iterator.
# To get a new list with the values multiplied by the given number,
# you can use lambda to create a simple function and pass it to map.

# In this implementation, map multiplies each element x in my_list by the specified number,
# and the list() function converts the resulting iterator into a new list.
# The original list my_list remains unchanged

# QUESTION
# Write a function that returns a list with all values multiplied by a number without using any loops.
# Prototype: def multiply_list_map(my_list=[], number=0):
# Returns a new list:
# Same length as my_list
# Each value should be multiplied by number
# Initial list should not be modified
# You are not allowed to import any module
# You have to use map
# Your file should be max 3 lines