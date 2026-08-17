class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        best = 0
  
        hashmap = {}


        while r < len(s):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)

            hashmap[s[r]] = r
            r += 1

            best = max(best, r - l)
        return best

