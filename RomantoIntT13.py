class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        flag = 1
        for i in range(len(s)):
            if flag == 0:
                flag = 1
                continue
            if i < len(s)-1:
                if s[i] == 'I' and s[i+1] == 'V':
                    total += 4
                    flag = 0
                    continue
                elif s[i] == 'I' and s[i+1] == 'X':
                    total += 9
                    flag = 0
                    continue
                elif s[i] == 'X' and s[i+1] == 'L':
                    total += 40
                    flag = 0
                    continue
                elif s[i] == 'X' and s[i+1] == 'C':
                    total += 90
                    flag = 0
                    continue
                elif s[i] == 'C' and s[i+1] == 'D':
                    total += 400
                    flag = 0
                    continue
                elif s[i] == 'C' and s[i+1] == 'M':
                    total += 900
                    flag = 0
                    continue
            if s[i] == 'I':
                total += 1
            elif s[i] == 'V':
                total += 5
            elif s[i] == 'X':
                total += 10
            elif s[i] == 'L':
                total += 50
            elif s[i] == 'C':
                total += 100
            elif s[i] == 'D':
                total += 500
            elif s[i] == 'M':
                total += 1000
            # else:
            #     return 0
        return total
    

s = Solution()
print(s.romanToInt("MCMXCIV"))