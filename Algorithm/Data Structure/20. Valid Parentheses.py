class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch = {"[":"]", "{":"}", "(":")"}
        for now in s:
            if now in ch.keys():
                stack.append(now)
            elif not stack or now != ch[stack[-1]]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True
