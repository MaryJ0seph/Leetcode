#Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

#MySolution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #j = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j]*2 and i!=j:
                    #if arr[j] >= 0:
                        print (arr[j])
                        print (arr[i])
                        return int
                        
#bestsolution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]] = i
        
        for i in range(len(arr)):
            if arr[i] * 2 in dic and i != dic[arr[i] * 2]:
                return True
        return False
        
#bestsolution2
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if 2 * i in seen or i % 2 == 0 and i #2 in seen:
                return True;
            seen.add(i)
        
        return False
