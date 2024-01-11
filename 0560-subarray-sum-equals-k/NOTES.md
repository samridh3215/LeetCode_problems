## My Approach

- To ceate a siding window and upadte the sum of the subarray as the window size increases or decreases
- The window size is modified based on the relation between current sum of sub array and k 

> Problem : My approach assumed the array would be sorted but it never mentioned anything about it and fails quite often when negative numbers are involved


## The better Approach

- Create a hashmap with a key value as (0, 1)
- As we go along the array we calculate the prefix sum of the element
- Now lets say we are at index `i` and the prefix sum is `preSum` we would like to find a subarray till the position `i` whose sum of elements is `k`.
- To achieve that we want to remove all the elements in the subarray whose sum is `preSum-k`, and hence we mantain count of number of occurences of `preSum-k` in hashmap
- We add the result with the no of occuronces of `preSum-k` 
