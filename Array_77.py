#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

#this could be done by pointer as well

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:       
        while nums.count(val):
            nums.remove(val)
            
            
#best solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k
