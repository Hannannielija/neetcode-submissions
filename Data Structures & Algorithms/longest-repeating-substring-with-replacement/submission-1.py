class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        frequency = 0
        best = 0

        count = {}
        while r < len(s):
            
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            frequency = max(count.values())

            while (r - l + 1) - frequency > k:
                count[s[l]] -= 1
                l += 1
            
            best = max(best, r - l + 1)
            r += 1
        
        return best

            





        