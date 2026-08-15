class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search

        l = 0
        m = len(nums) // 2
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) //2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1 
            else:
                r = m - 1
                

        return -1








        