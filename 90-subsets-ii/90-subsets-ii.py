class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def sub(index, arr):
            ans.append(arr[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                sub(i+1, arr)
                arr.pop()
        sub(0, [])
        return ans
    