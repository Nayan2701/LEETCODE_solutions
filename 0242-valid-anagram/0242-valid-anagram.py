
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Array to store character counts for 'a' through 'z'
        count = [0] * 26
        
        for i in range(len(s)):
            # ord(char) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # If any element is not 0, the strings are not anagrams
        for val in count:
            if val != 0:
                return False
                
        return True