class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict1 = set(nums)
        b_repeat = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in dict1:
                number = nums[i]
                repeat = 1
                while number + 1 in dict1:
                    number +=1
                    repeat +=1
                
                if repeat > b_repeat:
                    b_repeat = repeat
        
        
        return b_repeat



                





