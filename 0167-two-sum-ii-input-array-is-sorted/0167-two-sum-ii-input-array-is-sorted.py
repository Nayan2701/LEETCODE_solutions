class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            res=numbers[l]+numbers[r]
            if res<target:
                l+=1
            elif res>target:
                r-=1
            elif res == target:
                return [l+1,r+1]
