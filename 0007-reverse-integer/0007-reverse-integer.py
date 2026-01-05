class Solution:
    def reverse(self, x: int) -> int:
                
        if x > 0:
            temp = str(x)
            temp = int(temp[::-1])
            if temp > 2147483647:
                return 0

            else:
                return temp

            

        elif x < 0:
            temp = str(abs(x))
            temp = int('-' + temp[::-1])
            if temp >= -2147483648:
                return temp

            else:
                return 0


        else:
            return 0
        