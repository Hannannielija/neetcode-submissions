class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tuper = set(nums)
        
        if len(nums) > len(tuper):
            return True
        else: 
            return False

