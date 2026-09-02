class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        top = max(piles)
        k = 1
        while k <= top:
            mid = (top + k)//2
            takes = sum(map(lambda x: self.ceil(x, mid), piles))
            if takes > h:
                k = mid + 1
            else:
                top = mid - 1
    
        return k

           
    def ceil(self, x, mid):
        if x % mid == 0:
            return x // mid
        return x // mid + 1

        

        
        