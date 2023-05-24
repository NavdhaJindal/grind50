class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_dict = {}
        for n in nums:
            n_dict[n] = n_dict.get(n, 0) + 1
            if n_dict[n] > len(nums) // 2:
                return n