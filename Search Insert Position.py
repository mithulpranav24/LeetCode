from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                print(mid)
            else:
                h = mid - 1
                print(mid)

print(Solution().searchInsert([1,3,5,7], 9))