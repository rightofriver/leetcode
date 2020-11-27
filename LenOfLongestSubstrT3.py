class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = []
        if s == "":
            return 0
        elif len(s) == 1:
            return 1 
        for i in range(len(s)):
            for k in range(i,len(s)):
                if k == i:
                    tempsubStr = s[i]
                    continue
                if tempsubStr.find(s[k]) == -1: # s[k] is not in tempsubStr
                    tempsubStr = tempsubStr + s[k]
                else:
                    subStr.append(tempsubStr)
                    break
                if k == len(s)-1:
                    subStr.append(tempsubStr)
        if subStr == []:
            return 1 
        big = len(subStr[0])
        for j in range(1,len(subStr)):
            if len(subStr[j]) > big:
                big = len(subStr[j])
        return big


s = Solution()
print(s.lengthOfLongestSubstring("adfsau"))