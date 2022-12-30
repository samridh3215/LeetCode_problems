class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        for i in nums:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i]+=1
        print(Map.items())
        freq = dict(sorted(Map.items(), key=lambda x: x[1], reverse=True))
        res = list(freq.keys())[:k]
        return res
