class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        array1 = [0] * len(nums)
        array2 = [0] * len(nums)
        kanan = 1
        kiri = 1

        for i in range(len(nums)):
            r = -i -1
            array1[i] = kiri
            array2[r] = kanan
            kiri *= nums[i]
            kanan *= nums[r]


        for hasil in range(len(nums)):
            result.append(array1[hasil]* array2[hasil])

        return result
            


