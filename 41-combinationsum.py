class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_list, cur_sum):
            # print(i)
            # print(cur_list)
            # print(cur_sum) 
            if cur_sum == target: 
                res.append(cur_list.copy())
                # print(cur_list.copy())
                # print("above list appended")
                return 
            if cur_sum > target: 
                return
            if i >= len(candidates):
                return

            cur_list.append(candidates[i])
            dfs(i, cur_list, cur_sum + candidates[i])
            cur_list.pop()
            dfs(i + 1, cur_list, cur_sum)

        dfs(0, [], 0)

        return res