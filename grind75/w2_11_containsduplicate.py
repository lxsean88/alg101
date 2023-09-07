  # time O(n), space O(n)
  def containsDuplicate(self, nums: List[int]) -> bool:
      hm = {}
      for num in nums:
          if num in hm:
              return True
          else:
              hm[num] = 1
      return False

##############
#
# to save time
#
# time O(nlogn), space(logn)
##############
  def containsDuplicate2(self, nums: List[int]) -> bool:
      nums.sort()
      for i in range(1, len(nums)):
          if nums[i] == nums[i-1]:
              return True
     return False
