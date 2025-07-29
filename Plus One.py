from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if 1 <= len(digits) <= 100 and 0 <= digits[-1] <= 9:
            i = len(digits) - 1
            while i>= 0:
                if digits[i] < 9:
                    digits[i] += 1
                    return digits

                digits[i] = 0
                i -= 1
            return [1] + digits
        else:
            return None


print(Solution().plusOne([1,2,3,4,5]))