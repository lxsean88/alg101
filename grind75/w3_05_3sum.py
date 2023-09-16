
def threeSuym(nums: List[int]) -> List[List[int]]:
    def twoSum(nums, left, right, target, rst):
        added_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if added_pair != (nums[left], nums[right]):
                    rst.append([-target, nums[left], nums[right]])
                added_pair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    rst = []
    nums = sorted(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i]== nums[i-1]:
            continue
        twoSum(nums, i+1, len(nums)-1, -nums[i], rst)
    return rst
