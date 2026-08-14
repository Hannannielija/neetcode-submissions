class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {"()", "{}", "[]"}

        for i in range(len(s)):
            if  s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else: 
                if stack == [] or stack[-1] + s[i] not in dict1:
                    return False

                stack.pop()
            

        return stack == []
# if s[i] == "]" and stack[-1] == "[" or s[i] == ")" and stack[-1] == "(" or s[i] == "}" and stack[-1] == "{" :
            # elif s[i] + stack[-1] in dict1:
            #     stack.pop()