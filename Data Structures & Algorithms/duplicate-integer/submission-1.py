from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter()
        for n in nums:
            if counter[n]:
                return True
            counter[n] += 1
        return False

        