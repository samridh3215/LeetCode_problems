class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)
        for num in nums:
            if (num-1 not in nums):
                currNum = num
                streak = 1

                while(currNum+1 in nums):
                    currNum += 1
                    streak += 1 
                best = max(best, streak)
        return best