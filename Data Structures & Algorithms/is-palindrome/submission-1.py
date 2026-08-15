import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        

        clean = s.strip("?")
        clean = re.sub(r'[^a-zA-Z0-9]', '', clean)
        clean = clean.lower()

        r = len(clean) - 1

        while r > l:
            if clean[l] != clean[r]:
                return False
            
            l += 1
            r -= 1
        
        return True



        