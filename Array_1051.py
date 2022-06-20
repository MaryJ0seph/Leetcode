#Height Checker
#A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
#You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
#Return the number of indices where heights[i] != expected[i].

#solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        expected=sorted(heights) 
        i=0      
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count +=1
        return count 
        
        
 #best
 class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h=sorted(heights)
        cnt=0
        for i in range(len(heights)):
            if sorted_h[i] != heights[i]:
                cnt+=1
        return cnt
