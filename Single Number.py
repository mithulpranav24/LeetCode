from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if 1 <= len(nums) <= 3 * 10**4:  # Use ** for exponentiation, not ^
            d = dict.fromkeys(nums, 0)
            for i in nums:
                d[i] += 1
            for key, value in d.items():
                if value == 1:
                    return key


Solution().singleNumber([1,2,3,4,1,2,3,4,5])




