class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Check if lengths are equal
        if len(s) != len(t):
            return False
        
        # create dict for each 
        dict_s = {}
        dict_t = {}
        
        # Count characters in s and t
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
            
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
            
        # Compare dictionaries
        return dict_s == dict_t