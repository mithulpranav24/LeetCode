from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Si = n * (n + 1) // 2
        Sa = sum(nums)
        return Si - Sa



