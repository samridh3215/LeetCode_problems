class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            head, tail = i+1, len(nums)-1
            while(head<tail):
                sum = nums[i]+nums[head]+nums[tail]
                if sum<0:
                    head += 1
                elif sum>0:
                    tail -=1
                else:
                    ans.append([nums[i], nums[head], nums[tail]])
                    head += 1
                    while head<tail and nums[head]==nums[head-1]:
                        head += 1
        return ans
