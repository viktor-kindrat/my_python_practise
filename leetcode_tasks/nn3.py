def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all_nums = nums1.copy()
        all_nums.extend(nums2.copy())
        all_nums.sort()
        print(all_nums)
        
        return all_nums[int((len(all_nums) - 1) / 2)] if len(all_nums) % 2 else (all_nums[int(len(all_nums) / 2)] + all_nums[int((len(all_nums) / 2) - 1)]) / 2
    
print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))