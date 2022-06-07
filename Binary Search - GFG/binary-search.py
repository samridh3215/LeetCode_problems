#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		r = n-1
		l = 0
		
		while(l<=r):
		    mid = (l+r)//2
		    if(k==arr[mid]):
		        return mid
		    elif(k<arr[mid]):
		        r = mid-1
		    else:
		        l= mid+1
        return -1
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends