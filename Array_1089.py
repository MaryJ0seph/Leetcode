#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
#Input: arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                i+=2
                arr.pop()
            else:
                i+=1
