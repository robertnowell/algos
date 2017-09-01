"""
param: array of ints
return: sum of largest contiguous subsequence

[-334, 2, 34, -4]

[1, 2, 3, 34, -3, -400, -3, 2, 5, 4, 2, -2 -4, 14]

[]

[1, 2, 3, 4, 5, -4, -2, -3, 3, 2]



iterate through this array
running sum



possibilities for input:
    -empty list
    -invalid (non-integer input)
    -list of all positive
    -list of all negative
    -lists of positive and negative integers
        -testing location of contiguous sum

"""

def max_contiguous_sum(nums):
    if not nums or not nums.isnumeric():
        return 0
    # sum up to and including current index
    max_to_current_index = nums[0]
    # highest sum we've encountered
    max_sum = nums[0]
    for num in nums[1:]:
        max_to_current_index = max(max_to_current_index + num, num)
        max_sum = max(max_sum, max_to_current_index)


print max_contiguous_sum([1, 2, 3, 34, -3, -400, -3, 2, 5, 4, 2, -2 -4, 14])