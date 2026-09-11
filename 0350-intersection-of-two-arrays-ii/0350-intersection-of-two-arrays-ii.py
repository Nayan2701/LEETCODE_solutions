class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        seen = []
        for num in nums1:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        
        for num in nums2:
            if num in d and d[num]>0:
                seen.append(num)
                d[num]-=1
        return seen