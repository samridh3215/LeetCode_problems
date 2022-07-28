class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        l1 = len(nums1)
        l2 = len(nums2)
        if(l1> l2):
            for i in range(len(nums1)):
                x = nums1.pop()
                if x in nums2:
                    l.append(x)
                    nums2.remove(x)
        else:
            for i in range(len(nums2)):
                x = nums2.pop()
                if x in nums1:
                    l.append(x)
                    nums1.remove(x)
                    
        return l
     
        