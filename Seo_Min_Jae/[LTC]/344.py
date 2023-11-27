# 투 포인터를 이용한 스왑
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬다운 방식
def reverseString(self, s: List[str]) -> None:
    s.reverse()
    # s = s[::-1] 공간 복잡도를 O(1)로 제한하다보니 변수 할당을 처리하는 데 제약이 있다.
    # s[:] = s[::-1] 과 같은 트릭으로 해결 가능하다.