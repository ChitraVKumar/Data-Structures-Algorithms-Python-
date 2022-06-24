# Algorithm
# 1. Create an empty words list to store the words and a list for space to track
# 2. Initialize the index i to zero.
# 3. Using while loop to check if i is withing the length of the string
# 4. if the letter at position is not a space
# 5. then equate the variable word_start to i
# 6. Again using while loop to check if i within the length of the string and also if it's not a space
# 7. incrementing the i value by 1 to the next character
# 8. Once the end of the word is reached or loop ends append the word to the list words.
# 9. at step 4, else if, its a space again increment position by 1
# 10. Finally return the list items in reverse order joined by space.


def rev_words(s):
    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])
        i += 1
    #result = print(words[::-1])
    return " ".join(reversed(words))
    #return result

res = rev_words("All the Best")
print(res)