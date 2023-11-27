class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for str in s:
            if str.isalpha():
                a += str.lower()
            elif str.isdigit():
                a += str
        b=a[::-1]
        if a == b:
            return True
        return False

# 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():   # 영문자와 숫자 판별
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True

# 데크 자료형 이용
def isPalindrome(self, s: str) -> bool:
    # 자료형 데트로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.appned(char.append())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

# 슬라이싱 이용
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]