s = "loveleetcode"
chars_count = dict()
chars = set()

for i in s:
    if i in chars_count:
        chars_count[i] += 1

    else:
        chars_count[i] = 1

print(chars_count)

for k, v in chars_count.items():
    if chars_count[k] == 1:
        chars.add(k)
print(chars)
def uni(c):
    for i in range(len(s)):
        if s[i] in chars:
            return i
    return -1
print(uni(chars))
