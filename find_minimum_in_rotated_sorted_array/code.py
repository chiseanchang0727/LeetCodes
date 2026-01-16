from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass

    def binary_search(nums):
        left, right = 0, len(nums)-1

        while right - left > 1:
            mid = (left + right) // 2


            if nums[mid] > nums[0]:
                left = mid
            else:
                right = mid

            return nums[right ]