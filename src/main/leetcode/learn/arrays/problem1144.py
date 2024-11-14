'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
'''

class Problem1144(object):
    def pivotIndex(self, nums):
        sum = 0
        sumRight = []
        for num in nums:
            sum += num
            sumRight.append(sum)
        sum = 0
        sumLeft = [0 for x in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            sum += nums[i]
            sumLeft[i] = sum
        for i in range(len(nums)):
            if sumLeft[i] == sumRight[i]:
                return i
        return -1