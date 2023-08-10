class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(sub_nums: List[int]) ->  List[List[int]]: 
            if len(sub_nums) == 0:
                return [[]]
            if len(sub_nums) == 1: 
                return [[sub_nums[0]]]

            last_el = sub_nums[-1]
            prev_perms = dfs(sub_nums[:-1])

            cur_perms = []
            for i in range(len(sub_nums)):
                for perm in prev_perms: 
                    cur_perms.append(perm[:i] + [last_el] + perm[i:])
        
            return cur_perms

        return dfs(nums)