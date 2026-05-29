import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower() 
        len_n = len(s)
            
        mid = len_n//2
        if len_n % 2 == 0:
            forward = s[:mid]
            back = s[mid:][::-1]
        else:
            forward = s[:mid]
            back = s[mid + 1:][::-1]

        for i in range(len(forward)):
            if back[i] != forward[i]:
                return False
        return True


        