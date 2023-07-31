class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        answer = [1] * len(nums)

        for i in range(1, len(nums)): 
            prefix[i] = prefix[i - 1] * nums[i - 1]
            postfix[len(nums) - i - 1] = postfix[len(nums) - i] * nums[len(nums) - i]

        for i in range(len(answer)): 
            answer[i] = prefix[i] * postfix[i]

        return answer