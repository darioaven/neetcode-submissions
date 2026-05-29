class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers) - 1
        left = 0
        sm = numbers[right] + numbers[left]
        while sm != target:
            if sm < target:
                left += 1
            else:
                right -= 1
            sm = numbers[right] + numbers[left]

        return [left + 1, right + 1]
            