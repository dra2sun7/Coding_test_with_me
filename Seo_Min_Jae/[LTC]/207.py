class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(j):
            if visited[j] == 1:
                return True
            elif visited[j] == -1:
                return False
            
            visited[j] = -1

            for x in dict[j]:
                if not dfs(x):
                    return False
            
            visited[j] = 1

            return True
        

        dict = collections.defaultdict(list)
        for a, b in prerequisites:
            dict[a].append(b)
        
        visited = [0] * numCourses

        for i in list(dict):
            if not dfs(i):
                return False
        
        return True