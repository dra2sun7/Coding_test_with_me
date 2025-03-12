class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, e):
            results.append(e[:])

            if len(e) == len(nums):
                return
            
            for i in range(index, len(nums)):
                e.append(nums[i])
                dfs(i+1, e)
                e.pop()
        
        results = []
        dfs(0, [])
        return results