class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for i in d:
            if d[i]>1:
                for j in range(d[i]-1):
                    nums.remove(i)
        return len(nums)