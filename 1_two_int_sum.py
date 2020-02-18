'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        d = target - nums[i]
        if d in nums[i+1:]:
            return i, nums.index(d, i+1)

    return 0, 0

#nums = [2, 7, 11, 15]
#target = 9

nums = [3,3]
target = 6

#nums = [3,2,4]
#target = 6

a, b = twoSum(nums, target)
print(a, b)