def maxSubArray(self, nums: List[int]) -> int:
        sum, max_sum = 0, -sys.maxsize
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            sum = max(0, sum)
        return max_sum
