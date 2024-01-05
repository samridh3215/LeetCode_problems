class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0 #create left and right ends of the window 
        win = 0 # window size, also the result 
        total = 0
        while(r<len(nums)):
            total += nums[r]   #sum of elements in window
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            win = max(win, r - l + 1)
            r += 1
        

        return win
        

