class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        win_sum = 0
        mini = float("inf")

        for r in range(len(nums)):
            win_sum += nums[r]

            while win_sum >= target:
                mini = min(mini, r - l + 1)
                win_sum -= nums[l]
                l += 1

        return 0 if mini == float("inf") else mini