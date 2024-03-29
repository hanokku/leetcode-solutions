# Sort colors (75): https://leetcode.com/problems/sort-colors/
# Pattern: two pointers

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1