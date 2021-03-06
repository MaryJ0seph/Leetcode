#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        loc=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[loc]=nums[i]
                loc+=1
        return loc  
        
#best solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for x in range (1, len(nums)):
            if nums[x] != nums[i]:
                i +=1
                nums[i] = nums[x]
        return i+1
