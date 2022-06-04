def finder(arr1, arr2):

    if len(arr1) != len(arr2):
        seen = []
        result=[]

        for num in arr1:
            if num in arr2:
                seen.append(num)

            else:
                result.append(num)

    print(result)
    print(seen)

finder([5,5,7,7], [5,7,7])