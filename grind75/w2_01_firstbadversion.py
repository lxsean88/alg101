
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end -1:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid -1):
                    return mid
                end = mid - 1
            else:
                start = mid + 1

        if isBadVersion(start):
            return start
        else:
            return end
