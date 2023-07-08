# https://leetcode.com/problems/two-sum/

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, n in enumerate(nums):
            hash_map[n] = index

        print(hash_map)

        for index, n in enumerate(nums):
            if ((target - n) in hash_map.keys()):
                if (hash_map[target-n] != index):
                    return [hash_map[target-n], index]