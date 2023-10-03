class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        rst = []
        if not intervals:
            return rst
        
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if not rst or rst[-1][1] < interval[0]:
                rst.append(interval)
            else:
                rst[-1][1] = max(rst[-1][1], interval[1])
        return rst
