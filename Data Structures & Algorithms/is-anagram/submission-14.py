class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char = [0]*26

        for c in range(len(s)):
            char[ord(s[c]) - ord('a')] += 1
            char[ord(t[c]) - ord('a')] -= 1
        
        for value in char:
            if value != 0:
                return False
        return True



        