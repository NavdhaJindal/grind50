class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum_at_prev = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if sum_at_prev > 0:
                sum_at_prev += nums[i]
            else:
                sum_at_prev = nums[i]
            
            maxSum = max(maxSum, sum_at_prev)
        
        return maxSum
         