
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev1 = 1
        prev2 = 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        for x in range(3, n+1):
            tmp = prev1 + prev2
            prev1 = prev2
            prev2 = tmp

        return prev2
