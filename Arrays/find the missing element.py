import collections
# def finder(arr1, arr2):
#
#     if len(arr1) != len(arr2):
#         seen = []
#         result=[]
#
#         for num in arr1:
#             if num in arr2:
#                 seen.append(num)
#
#             else:
#                 result.append(num)
#
#     print(result)
#     print(seen)
#
# finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])#-Sucess
#finder([5,5,7,7], [5,7,7])#failed

# NlogN solution:

# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#
#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1
#
#     return arr1[-1]

# solution using hash tables

def finder(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1

res = finder([5,5,7,7], [5,7,7])
print(res)

# def finder3(arr1, arr2):
#     result = 0
#
#     for num in arr1+arr2:
#         result ^= num
#         print(result)
#
#     return result
#
# finder3([5,5,7,7], [5,7,7])

