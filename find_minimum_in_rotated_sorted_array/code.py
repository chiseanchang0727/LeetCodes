from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        We compare nums[mid] with nums[right] to determine
        which sorted segment mid belongs to.

        Invariant:
        - nums[right] always lies in the right sorted segment
        - The minimum is the only place where the order breaks

        Why nums[mid] < nums[right] works:
        - nums[mid] < nums[right] means mid is in the right sorted segment
        - The minimum is ≤ nums[mid]
        - Therefore, the minimum is in [left, mid]
        - We set right = mid (keep mid)

        Why nums[mid] > nums[right]:
        - mid lies in the left sorted segment
        - The minimum must be to the right of mid
        - We set left = mid + 1

        Why not compare with nums[0]:
        - nums[mid] > nums[0] only tells us mid is in the left sorted segment
        - This fails for non-rotated arrays like [0,1,2,3,4]
        - nums[right] is a stable reference point for the rotation
        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            # Compare mid and right: find minimum
            # If right half is sorted, minimum is in left half (including mid)
            if nums[mid] < nums[right]:
                right = mid  # Keep mid, as it might be the minimum
            else:
                # Right half contains rotation point, minimum is in right half
                left = mid + 1

        return nums[right]



solution = Solution()
ans = solution.findMin(nums=[11,13,15,17])
print(ans)