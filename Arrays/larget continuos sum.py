# 1. if nums are all positive then sum is the largest
# Algorithm;
# 1. We start summing up the numbers and store in a current sum variable.
# 2. After adding each element, we check if current sm is large than maximun sum encountered so far.
# 3. If it is, we update the maximun sum.
# 4. As long as the current sum is positve, we keep adding the numbers.
# 5. When the current um becomes negative, we start with a new current sum. coz negative current sum will only decrease the sum of a future sequence.
# 6. Note that we dont reset the current sum to 0 because the array can contain all negative integers. Then te result would be largest negative integer.

def large_cont_sum(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        i = current_sum + num
        current_sum = max(i, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

res = large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
print(res)