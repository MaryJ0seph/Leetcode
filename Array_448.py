#Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:    
        n = len(nums)
        numbers_set = set(range(1, n + 1))

        for i in nums:
            if i in numbers_set:
                numbers_set.remove(i)

        return numbers_set
        
        
 #best
 class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ll=len(nums)  
        ss=[]
        nn=set(nums)
        for i in range(1,ll+1):
            if i not in nn:
                ss.append(i)
        return ss 
