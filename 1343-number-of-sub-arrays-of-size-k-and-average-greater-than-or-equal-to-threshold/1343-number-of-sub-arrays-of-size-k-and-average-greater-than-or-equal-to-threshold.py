class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[:k-1])   #Calculate sum of inital window as window size is always constant 
        for l in range(len(arr)-k+1):  # l is the left pointer and right pointer is l + k
            currSum += arr[l+k-1]   # maintain running sum
            if(currSum/k >= threshold):
                count+=1
            currSum -= arr[l]   #maintain running sum 
        return count
            