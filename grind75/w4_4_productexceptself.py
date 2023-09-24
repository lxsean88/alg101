class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1
        
        ans = []
        for num in nums:
            if not zeros:
                ans.append(product//num)
            else:
                if num != 0:
                    ans.append(0)
                else:
                    if zeros == 1:
                        ans.append(product)
                    else:
                        ans.append(0)
        
        return ans
            
        
