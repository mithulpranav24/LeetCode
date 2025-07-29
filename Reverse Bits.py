class Solution:
    def reverseBits(self, n: int) -> int:
        if 0 <= n <= (2**31)-2 and n % 2 == 0:
            s = str(format(n & 0xFFFFFFFF, '032b'))
            sr = s[::-1]
            return int(sr, 2)


print(Solution().reverseBits(2147483644))

#print((2**31)-2)



