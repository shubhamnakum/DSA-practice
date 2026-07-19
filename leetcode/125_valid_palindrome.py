"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


# Naive : 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for char in s: 
            if char.lower().isalnum():
                temp.append(char.lower())
        temp_str = "".join(temp)
        n = len(temp_str)
        for i in range(n//2):
            if (temp_str[i] != temp_str[n-1-i]):
                return False
        return True


