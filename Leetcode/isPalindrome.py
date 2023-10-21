class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        else:
            num = x
            reversed_num = 0

            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10
            if x == reversed_num:
                return True
        
"""
Runtime: 61ms
Memory: 16MB
"""