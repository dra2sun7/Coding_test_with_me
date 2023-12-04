class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        p = s[::-1]
        for i in range(len(s)):
            if s[i] == p[i]:
                answer += s[i]
        return answer

# 정답
def longestPalindrome(self, s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            return s[left+1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s)-1):
        result = max(result,
                        expand(i, i+1),
                        expand(i, i+2),
                        key=len)
    
    return result