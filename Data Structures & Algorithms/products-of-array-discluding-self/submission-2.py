class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_n = len(nums)

        prefix = [1] * len_n


        for i in range(len_n):
            if i != 0:
                prefix[i] = nums[i-1] * prefix[i-1]
            else:
                prefix[i] = 1

        suffix = 1
        print(prefix)
        for i in range(len_n - 1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]
        
        return prefix