class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        return_list = []

        for i, num in enumerate(nums):
            if num > 0:
                return return_list
            if i > 0:
                prev = nums[i - 1]
                if num == prev: 
                    continue
            if i <= len(nums) - 3: 
                p1 = i + 1
                p2 = len(nums) - 1
                while p1 < p2: 
                    cur_sum = nums[p1] + nums[p2]
                    if (cur_sum == -num):
                        return_list.append([num, nums[p1], nums[p2]])
                        p1 += 1
                        while nums[p1] == nums[p1 - 1] and p1 < p2:
                            p1 += 1
                    elif (cur_sum < -num):
                        p1 += 1
                    elif (cur_sum > -num):
                        p2 -= 1

        return return_list