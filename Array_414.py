#Third Maximum Number
#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

#solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        unique.sort(reverse = True)
        n=len(unique)-1
        if len(unique) > 2:
            print(n)
            return unique[2]
        else:
            return max(unique)
            
#best
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new = list(set(nums))
        new.sort()
        print(new)
        if(len(new) < 3 or new[len(new)-2] == new[len(new)-1] or new[len(new)-2] == new[len(new)-3] ):
            m = new[len(new)-1]
        else:
            m  = new[-3]
        return m
        
 #best2
 class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hash = sorted(set(nums))
        if len(hash) >= 3:
            return hash[-3]
        else:
            return max(hash)
