# My solution
# s1 = "clint eastwood"
# s2 = "old west action"

# for i in s1:
#     if sorted[s1]==sorted[s2]:
#         print(True)
#     else:
#         print(False)

# Second Solution
# def anagram2(s1, s2):
#     # remove space from both the string and convert into lower case
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()

#     return sorted(s1) == sorted(s2) # if they are sorted and equal return true

# res = anagram2('good', 'dog')
# print(res)

# Best Solution
def anagram3(s3, s4):
    s3 = s3.replace(" ", "").lower()
    s4 = s4.replace(" ", "").lower()

    # Edge case check
    if len(s3) != len(s4):
        return False

    count = {}  # count the frequency of each letter and store that in this dict.

    for letter in s3:
        if letter in count:
            count[letter] += 1
        
        else:
            count[letter] = 1
    
    for letter in s4:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

result = anagram3('clint eastwood', 'old west action')
print(result)



    