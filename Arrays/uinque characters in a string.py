#s = "hello"
#
# res = ''.join(sorted(s))
# print(res)
# chars = []
#
# for i in range(1, len(res)):
#     if res[i] != res[i-1]:
#         print(False)
#     else:
#         chars.append(res[i])
# print(chars)
# print(True)

def unique(s):
    chars = set()

    for let in s:
        if let not in chars:
            chars.add(let)
        else:
            return False
    return True

print(unique("hello"))