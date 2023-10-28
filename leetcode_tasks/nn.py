def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        for idx, value in enumerate(nums):
            print(nums[idx - 1], value, nums[idx - 1] < target, target < value)
            if idx > 0 and nums[idx - 1] < target and target < value:
                return idx
        return len(nums)
            
print(searchInsert([1,3,5,6], 7))