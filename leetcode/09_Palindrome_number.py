"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# Naive Mathematical Approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        org_num = x
        rev = 0
        if x<0 :
            return False
        while (x>0):
            remainder = x%10
            rev = (rev * 10) + remainder
            x = int(x/10)
        print(rev)
        if rev == org_num:
            return True
        else:
             return False
        
# TC --> O(d)  //no of digits
# TC --> O(1)

# Recursion Approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        if x < 0 : 
            return False
        for i in range(0,int(n/2)):
            if (s[i] != s[n-1-i]):
                return False
        return True

# TC --> O(d/2)  // no of digits
# SC --> o(1)