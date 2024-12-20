class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Check if the length of the string is even
        if len(s) % 2 != 0:
            return False
        
        # Iterate through the string to find a substring that is a palindrome
        for i in range(1, len(s) // 2 + 1):
            # If the substring is a palindrome, check if it is a repeated pattern
            if s[:i] * 2 == s:
                return True
        
        return False

            