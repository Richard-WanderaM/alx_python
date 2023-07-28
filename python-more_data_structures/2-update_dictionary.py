# Update the dictionary with the given key-value pair

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# We implement the update_dictionary function by simply updating the given key with 
# the provided value in the dictionary.
# If the key does not exist in the dictionary, you can add it with the given value

#QUESTION
# Write a function that replaces or adds key/value in a dictionary.

# Prototype: def update_dictionary(a_dictionary, key, value):
# key argument will be always a string
# value argument will be any type
# If a key exists in the dictionary, the value will be replaced
# If a key doesn’t exist in the dictionary, it will be created
# You are not allowed to import any module