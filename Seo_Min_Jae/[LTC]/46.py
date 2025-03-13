class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num, e):
            if len(e) == len(nums):
                results.append(e[:])
                return

            for n in num:
                ne = num[:]
                ne.remove(n)

                e.append(n)
                dfs(ne, e)
                e.pop()

        results = []
        dfs(nums, [])
        return results