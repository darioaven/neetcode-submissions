class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        print(product)

        for i,j in enumerate(nums):
            for i2, j2 in enumerate(product):
                if i != i2:
                    product[i2] *= j

        return product