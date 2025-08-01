from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ip = 0
        for i in nums:
            if i != 0:
                nums[ip] = i
                ip += 1

        for i in range(ip,len(nums)):
            nums[i] = 0