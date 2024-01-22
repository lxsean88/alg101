class Solution:
    def helper(self, nums, rst, rsts, visited):
        if len(rst) == len(nums):
            rsts.append(list(rst))
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            rst.append(nums[i])
            visited[i] = True
            self.helper(nums, rst, rsts, visited)
            visited[i] = False
            rst.pop()

        


    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results
        visited = [0] * len(nums)
        self.helper(nums, [], results, visited)
        return results
