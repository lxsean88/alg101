class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rsts = []
        candidates = sorted(candidates)
        self.helper2(candidates, target, 0, [], rsts)
        return rsts

    def helper(self, candidates, target, start, rst, rsts):
        if target < 0:
            return
        if target == 0:
            rsts.append(list(rst)) 
            return
        
        for i in range(start, len(candidates)):
            rst.append(candidates[i])
            self.helper(candidates, target-candidates[i], i, rst, rsts)
            rst.pop()
    

    def helper2(self, candidates, target, cur, rst, rsts):
        if target < 0:
            return
        if target == 0:
            rsts.append(list(rst)) 
            return
        if cur >= len(candidates):
            return
      
        rst.append(candidates[cur])
        self.helper2(candidates, target-candidates[cur], cur, rst, rsts)
        rst.pop()
        self.helper2(candidates, target, cur+1, rst, rsts)
