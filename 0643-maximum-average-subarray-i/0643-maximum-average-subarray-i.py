class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l=0
        win_sum=0
        maxi = float("-inf")
        for r in range(len(nums)):
            win_sum+=nums[r]

            if r-l+1>k:
                win_sum-=nums[l]
                l+=1
            if r-l+1 == k:
                maxi=max(maxi,win_sum)
        return maxi/k