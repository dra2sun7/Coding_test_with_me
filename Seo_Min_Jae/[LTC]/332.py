class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(dep):
            while dict[dep]:
                dfs(dict[dep].pop(0))
            results.append(dep)
        
        dict = collections.defaultdict(list)
        for f, t in sorted(tickets):
            dict[f].append(t)
        
        results = []

        dfs('JFK')

        return results[::-1]