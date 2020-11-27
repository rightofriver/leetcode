class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = int(x)  #FIXIT
        #  TypeError: '<' not supported between instances of 'str' and 'int'
        if x < 0 or x > 2147483647:
            return False
        y = 0
        temp = x
        while x != 0:
            last = x % 10
            x = (int)(x/10)
            y = y*10 + last
        if y == temp:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome("121"))