class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(index, e):
            if len(e) == k:
                results.append(e[:])
                return
            
            for i in range(index, n+1):
                e.append(i)
                dfs(i+1, e)
                e.pop()

        results = []
        dfs(1, [])
        return results