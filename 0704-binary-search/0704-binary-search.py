class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if(len(nums)==1 and target==nums[0]):
            return 0
        while(l<=r):
            i= l + ((r - l) // 2)
            if(target == nums[i]):
                return i
            elif (target>nums[i]):
               l = i+1
            else:
               r = i-1
            # print(l, r)
        return -1