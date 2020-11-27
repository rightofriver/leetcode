class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < -(2**31) or x > (2**31)-1:
            return 0
        if x < 0:
            x = -x
            flag = 0
        elif x == 0:
            return x
        y = 0  # reverse number
        while x != 0:
            last = x % 10
            x = int((x - last)/10)
            y = y * 10 + last
        if flag == 0 and y <= (2**31):
            return -y
        elif flag == 1 and y <= (2**31)-1:
            return y
        else:
            return 0

s = Solution()
print(s.reverse(1534236469))