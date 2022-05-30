def arraypairsum(arr, k):
    
    if len(arr) < 2:
        return "Error! Less than two elements in the aaray!"

    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add( ( (min(num, target)), (max(num, target)) ) )

    print(len(output))
    return '\n'.join(map(str, list(output)))

res = arraypairsum([1, 3, 2, 2], 4)
print(res)









# # my dumb solution 1
# arr = [(1,3,2,2), 4]
# k = arr[1]
# # count = []
# for i in range(0,1):
#     for j in range(1,4):
#         if arr[i][j] + arr[i][j+1] == k:
#             print('({},{})'.format(arr[i][j], arr[i][j+1]))
# # print(count)

