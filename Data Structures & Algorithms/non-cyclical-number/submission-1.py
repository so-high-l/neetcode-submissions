class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        

        while n != 1 :
            print("n: ", n)
            square = 0
            for digit in str(n):
                d = int(digit)
                square += d * d
            print("square is : ", square)            
            
            if square == 1:
                return True
            elif square in seen:
                return False
            else:
                seen.add(square)
                n = square

        return True