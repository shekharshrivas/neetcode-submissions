class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3

        first = 2
        second = 3
        for i in range(4, n+1):
            temp = first + second
            first = second
            second = temp
        return second
        