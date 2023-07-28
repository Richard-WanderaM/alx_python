def best_score(a_dictionary):
    # Check if the dictionary is None or empty
    if a_dictionary is None or not a_dictionary:
        return None

    # Initialize variables to track the maximum value and its corresponding key
    max_value = None
    max_key = None

    # Loop through the dictionary to find the maximum value and its key
    for key, value in a_dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key

    return max_key

# To find the key with the biggest integer value in the dictionary, 
# We then loop through the dictionary and keep track of the maximum value and its corresponding key.

#QUESTION

# Write a function that returns a key with the biggest integer value.

# Prototype: def best_score(a_dictionary):
# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score
# You are not allowed to import any module