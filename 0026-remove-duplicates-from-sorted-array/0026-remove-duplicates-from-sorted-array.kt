class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var r = 0; var l = 0; var i = 0;
        while(r<nums.size){
            while(r<nums.size && nums[r] == nums[l]){
                r++;
            }
            nums[i] = nums[l]
            i++
            l = r
        }
        return i
    }
}