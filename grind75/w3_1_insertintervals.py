
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i, l = 0, len(intervals)
    rst = []
    while i < l and intervals[i][1] < newInterval[0]:
        rst.append(intervals[i])
        i += 1

    while i < l and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = min(newInterval[1], intervals[i][1])
        i += 1
    rst.append(newInterval)

    while i < l:
        rst.append(intervals[i])
        i += 1
    return rst

