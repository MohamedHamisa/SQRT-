class Solution:
    def mySqrt(self, x: int):
        r = x   # avoid dividing 0
        while r*r > x:
                r = int((r + x//r) // 2)  # newton's method
        return r
