class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, e):
            if len(e) == len(digits):
                results.append(e)
                return
            
            for d in range(index, len(digits)):
                for i in range(len(nums[digits[d]])):
                    dfs(d+1, e + nums[digits[d]][i])
        
        nums = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], 
                "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        
        results = []

        if not digits:
            return results
            
        dfs(0, '')

        return results