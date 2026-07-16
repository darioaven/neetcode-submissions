from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        response = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                n1 = nums[i]
                n2 = nums[j]

                counter[n1] -= 1
                counter[n2] -= 1
                val = -1 * (n1 + n2)
                if counter[val] > 0:
                    tp = tuple(sorted([n1,n2,val]))
                    response.add(tp)
                counter[n1] += 1
                counter[n2] += 1
        return_list = [list(i) for i in response]
        return return_list