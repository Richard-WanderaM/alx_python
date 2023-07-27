def multiple_returns(sentence):
    if not sentence:
        return 0, None
    else:
        return len(sentence), sentence[0]

# if not sentence:: This checks if the sentence is empty. An empty string evaluates to False, so this condition is true when sentence is empty.

# return 0, None: If the sentence is empty, the function returns a tuple with the length 0 and the first character as None.

# else:: If the sentence is not empty, the function proceeds to the next part.

# return len(sentence), sentence[0]: If the sentence is not empty, the function returns a tuple with the length of the sentence and the first character of the sentence.