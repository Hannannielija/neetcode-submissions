class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len (heights) - 1

        big = 0

        while r > l:
            lebar = r - l

            big = max(big, lebar * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: r -= 1

        return big



        