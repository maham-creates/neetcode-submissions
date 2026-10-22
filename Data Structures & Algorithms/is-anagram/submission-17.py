class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        charlist = [0]*26

        for char in s:
            charlist[ord(char)-ord('a')] += 1 # assuming s and r are lowercase letters
        
        for char in t:
            charlist[ord(char)-ord('a')] -= 1
        
        for num in charlist:
            if num != 0:
                return False
        return True




            
