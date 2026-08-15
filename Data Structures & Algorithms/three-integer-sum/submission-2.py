class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array1 = sorted(nums)
        result = []


        for i in range(len(array1)):
            l = i + 1
            r = len(array1) -1 

            if i > 0:
                if array1[i -1] == array1[i]:
                    continue

            while r > l:

                if array1[i] + array1[l] + array1[r] > 0:
                    r -= 1
                elif array1[i] + array1[l] + array1[r] < 0:
                    l += 1
                elif array1[i] + array1[l] + array1[r] == 0:
                    result.append([array1[i], array1[l], array1[r]])
                    r -=1
                    l +=1
                    while array1[r + 1] == array1[r] and r > l:
                        r -= 1
                    while array1[l - 1] == array1[l] and r > l:
                        l += 1
                    

        return result
            



        

