#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

#old -long run time
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newnums=[None]*5
        for i in range(len(nums)):
            newnums[i]=nums[i]*nums[i]
        return sorted(newnums)    
        
#new
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #create new array
        newnums=[0]*len(nums)
        
        #create pointer with their start position
        left=0
        right=len(nums)-1
        loc=right
        
        #if left and right are stil far away, take the square root
        while left <= right:
            leftsq=nums[left]*nums[left]
            rightsq=nums[right]*nums[right]
            
            #compare the square roots
            if leftsq <= rightsq:
                newnums[loc]=rightsq
                loc-=1
                right-=1
            else:
                newnums[loc]=leftsq
                loc-=1
                left+=1
        
        #get result
        return newnums
