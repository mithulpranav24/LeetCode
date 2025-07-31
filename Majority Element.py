from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for k in count:
            if count[k] > len(nums) // 2:
                return k

print(Solution().majorityElement([1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3]))