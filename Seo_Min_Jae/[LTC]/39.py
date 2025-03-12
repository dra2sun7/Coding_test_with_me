class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, e,t):
            if t == 0:
                results.append(e[:])
                return
            
            if t < 0:
                return
            
            if t > 0:
                for i in range(index, len(candidates)):
                    e.append(candidates[i])
                    dfs(i, e, t - candidates[i])
                    e.pop()

        results = []
        dfs(0, [], target)
        return results