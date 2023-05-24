class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
    
#         n_dict = {}
#         for n in nums:
#             n_dict[n] = n_dict.get(n, 0) + 1
#             if n_dict[n] > len(nums) // 2:
#                 return n

