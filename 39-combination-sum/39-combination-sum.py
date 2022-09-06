class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        def get_combinations(ind, target, arr, result):
            if ind == len(arr):
                if target == 0:
                    final.append(result[0:len(result)])
                return
            if arr[ind] <= target:
                result.append(arr[ind])
                get_combinations(ind, target-arr[ind], arr, result) 
                result.pop()
            get_combinations(ind+1, target, arr, result)  
        get_combinations(0, target, candidates, [])
        return final
                