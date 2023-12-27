class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        iteration = []

        def kSum(k, start, target):
            if k!= 2: 
                for i in range(start, len(nums)-k+1):
                    if(i>start and nums[i]==nums[i-1]):  # this is checked to prevent duplicates
                        continue 
                    iteration.append(nums[i])
                    kSum(k-1, i+1,target-nums[i])
                    iteration.pop()
                return 
            else:
                l, r = start, len(nums)-1
                while l<r:
                    if nums[l]+nums[r]<target:
                        l+=1
                    elif nums[l]+nums[r]>target:
                        r-=1
                    else:
                        res.append(iteration+[nums[l], nums[r]])
                        l+=1
                        while(l<r and nums[l] == nums[l-1]): #to check duplicates and out of bounds 
                            l+=1
        nums.sort()
        kSum(4, 0, target)
        return res