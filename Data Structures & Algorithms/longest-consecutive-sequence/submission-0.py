from collections import Counter
import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        cons = 0
        pointer = 0
        mx = 0
        for i, n in enumerate(nums):
            if i == 0:
                cons += 1
            else:
                if n == nums[i-1] + 1:
                    cons += 1
                else:
                    if n != nums[i-1]:
                        cons = 1
            if cons > mx:
                mx = cons

        return mx

        