def subsets(nums: List[int]) -> List[List[int]]:
    results = []
    # optional
    nums = sorted(nums)
    dfs(nums, 0, [], results)
    return results

def dfs(nums, index, rst, rsts):
    if index == len(nums):
        rsts.append(list(rst))
        return
    rst.append(nums[index])
    dfs(nums, index + 1, rst, rsts)
    rst.pop()
    dfs(nums, index + 1, rst, rsts)

def dfs2(nums, index, rst, rsts):
    rsts.append(list(rst))
    for i in range(index, len(nums)):
        rst.append(nums[i])
        dfs2(nums, i+1, rst, rsts)
        rst.pop()
