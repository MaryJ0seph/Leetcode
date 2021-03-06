#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        
        for r in range(len(nums)):
            if nums[r] %2 == 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums 
        
        
#best
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
