class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer  = {}
        stack =[]
        result = []

        for i in nums2:
            while stack and i>stack[-1]:
                answer[stack.pop()]=i
            stack.append(i)

        for i in nums1:
            if i in answer:
                result.append(answer[i])
            else:
                result.append(-1)
        
        return result
            
            