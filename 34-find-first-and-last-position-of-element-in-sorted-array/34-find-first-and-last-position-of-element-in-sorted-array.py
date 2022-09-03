class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin(a, low, high, target):
            if (nums ==[] or target>nums[-1]):
                return [-1,-1]
            while(low<=high):
                mid = (low+high)//2
                if a[mid]== target:
                    i, j = mid, mid
                    while(i>=0 and a[i] == target):
                        i-=1
                    while(j<len(nums) and a[j]==target):
                        j +=1
                    return [i+1, j-1]
                elif(a[mid]>target):
                    return bin(a, low, mid-1, target)
                else:
                    return bin(a, mid+1, high, target)
                
            return [-1, -1]
        return(bin(nums, 0, len(nums), target))