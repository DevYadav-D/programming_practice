'''
Third Maximum Number

Solution
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''

class Problem3231(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        non_repeated_nums = []
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                non_repeated_nums.append(nums[i])
        # print(non_repeated_nums)
        if len(non_repeated_nums)<3:
            return nums[-1]
        else:
            return non_repeated_nums[-3]