class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range (0,x+1):
            if i*i > x:
                return i-1


print(Solution().mySqrt(145))

