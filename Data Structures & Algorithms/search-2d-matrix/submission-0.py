class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [x for sub in matrix for x in sub]
        print(arr)
        low = 0
        high = len(arr) - 1
        while low <= high:

            mid = low + (high - low)//2
            x = arr[mid]

            if x == target:
                return True
            elif x > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return False
        