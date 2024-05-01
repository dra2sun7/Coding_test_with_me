from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = Counter(jewels)
        answer = 0
        
        for stone in stones:
            if stone in jewel:
                answer += 1
        
        return answer