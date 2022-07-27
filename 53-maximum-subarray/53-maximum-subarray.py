class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return sum(nums)
        Sums = []
        curr = nums[0]
        for x in nums[1:]:
            if (curr+x > x) and (curr+x > curr):
                curr+=x
            else:
                Sums.append(curr)
                curr = max(curr+x, x)
                
        Sums.append(curr)
        return max(Sums)