class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while n != 1 :
            square = 0
            for digit in str(n):
                d = int(digit)
                square += d * d
            
            if square in seen:
                return False
            else:
                seen.add(square)
                n = square

        return True