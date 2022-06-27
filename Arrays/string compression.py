# s = 'AAAABaa'
# count = dict()
# for i in s:
#     if i in count:
#         count[i] += 1
#
#     else:
#         count[i] = 1
#
# res = print(''.join(f'{k}{v}' for k, v in count.items()))

# Algorithm
# 1. Initialize empty string r, variable count = 1 and an index marker i = 1.
# 2. Two edge cases:
#   1. If the length of the string is empty return empty string
#   2. If the length of the string is 1 the return concatenated string+"1"(Ex:A1)
# 3. While i < length of the string
#   1. if current character s[i] is equal to the previous char s[i-1] then
#       count = count + 1 increase the count value
#   2. else (if s[i] != s[i-1])
#       r = r + s[i-1] + str(count)
#       count = 1 reset the count to 1
#   3. Increment the index value i = i + 1 till while loop terminates
# 4. r = r + s[i-1] + str(count)
# 5. return r


def compress(s):
    r = ''
    count = 1
    i = 1

    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s + "1"

    while i < len(s):
        if s[i] == s[i-1]:
            count += 1

        else:
            r = r + s[i-1] + str(count)
            print(r)
            count = 1

        i += 1

    r = r + s[i-1] + str(count)
    return r

res = compress('AAAABaa')
print(res)







