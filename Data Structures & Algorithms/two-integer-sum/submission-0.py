from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = dict()
        for i, n in enumerate(nums):
            difference = target - n
            if difference in ind:
                return [ind[difference], i]
            ind[n] = i        
        