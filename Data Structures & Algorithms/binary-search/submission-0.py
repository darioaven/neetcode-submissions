class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ind = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            
            mid = low + (high - low)//2
            n = nums[mid]
            if n == target:
                return mid
            
            elif n > target:
                high = mid - 1
            
            else:
                low = mid + 1

        return ind