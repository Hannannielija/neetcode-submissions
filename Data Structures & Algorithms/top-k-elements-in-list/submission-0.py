class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = {

        }
        bucket = [[]for _ in range(len(nums)+ 1)]


        for i in range(len(nums)):

            if nums[i] in dict1:  
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        
        for x, y in dict1.items():
            bucket[y].append(x)


        result = []
        j = len(bucket) -1   
        
        while k != len(result):
            if bucket[j] == []:
                j -= 1
            else:
                result.extend(bucket[j])
                j -= 1

        
        return result
            

