class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        char_arrayS = list(s)
        char_arrayT = list(t)
        char_arrayS.sort(key=ord)
        char_arrayT.sort(key=ord)

        return char_arrayS == char_arrayT