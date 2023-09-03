
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hm = {}
    for index, num in enumerate(nums):
        if target - num[index] in hm:
            return [index, hm[target-num[index]]]
        else:
            hm[target-numb[index]] = index
    return []
