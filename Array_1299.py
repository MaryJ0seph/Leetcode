#Replace Elements with Greatest Element on Right Side
#Input: arr = [17,18,5,4,6,1]
#Output: [18,6,6,6,1,-1]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #given in question
        lastval = -1
        #for loop starts from decreasing order till -1 (-1 is not included so it ends till 0)
        for i in range(len(arr)-1, -1, -1):
            #compare original value with -1. we take this value and keep before we overwrite 
            newval = max(lastval, arr[i])
            #save the max value in array
            arr[i] = lastval
            #save it for further process
            lastval = newval
        return arr 
        
#best solution
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        largest=arr[n-1]
        arr[n-1]=-1
        for i in range(n-2,-1,-1):
            temp=arr[i]
            arr[i]=largest
            if temp>largest:
                largest=temp
        return arr
