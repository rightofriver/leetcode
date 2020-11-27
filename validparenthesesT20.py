class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue
            elif s[i] == ')' and len(stack) != 0 and stack[len(stack)-1] == '(':
                stack.pop()
            elif s[i] == ']' and len(stack) != 0 and stack[len(stack)-1] == '[':
                stack.pop()
            elif s[i] == '}' and len(stack) != 0 and stack[len(stack)-1] == '{':
                stack.pop()
            else:
                return False
        return stack == []

s = Solution()
print(s.isValid("))"))