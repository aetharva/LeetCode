class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp = x
        rev = 0
        1323
        while(x > 0):
            digi = x % 10
            rev = rev*10 + digi
            x = x//10
        
        return temp == rev