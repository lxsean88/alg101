def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start < end - 1:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if nums[start] == target:
        return start
    if nums[end] = target:
        return end
    return -1

