class Solution:
    def reverse(self, x: int) -> int:
        if x in range(-2**31, 2**31 - 1) :
            if x <0 :
                num = str(x)
                rev = num [1:]
                rev = rev [::-1]
                res = -int(rev)
            
            else :
                num = str(x)
                rev = num [::-1]
                res = int(rev)
            if res in range(-2**31, 2**31 - 1) :
                return res
            else :
                return 0
        else :
            return 0



            