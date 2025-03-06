class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = collections.Counter(nums)
        answer = []

        for n, c in dict.most_common(k):
            answer.append(n)
        
        return answer
