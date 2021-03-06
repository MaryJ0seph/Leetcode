#Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        i=0
        j=n-1
        
        if n<3:
            return False
        
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
                
        while j > 0 and arr[j] < arr[j-1]:
            j -= 1
        
        return i==j and 0 < i and j < n-1
        
#best
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        if len(arr) <= 2:
            return False
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                left = i
            elif arr[i-1] == arr[i]:
                return False
            else:
                break
        print(left)
        right = len(arr) - 1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] > arr[i]:
                right = i - 1
            elif arr[i-1] == arr[i]:
                return False
            else:
                break
        print(right)
        if right == len(arr)-1 or left == 0:
            return False
        return left == right
