#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums  
        
#best
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        if m>1:
            idl = 0
            for idr in range(m):
                if nums[idr]!=0:
                    nums[idr],nums[idl] = nums[idl],nums[idr]
                    idl+=1
