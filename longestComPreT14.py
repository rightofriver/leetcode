from typing import List 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        j = 0
        if strs == []:
            return s
        small = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < small:
                small = len(strs[i])
        for j in range(small):
            for k in range(len(strs)):
                pre = strs[0][j]
                if pre == "":
                    return s
                if strs[k][j] == pre:
                    continue
                else:
                    return s
            s = s + pre
        return s


s = Solution()
print(s.longestCommonPrefix([]))