# 내 풀이 -> 오답
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        letter_logs = []
        digit_logs = []
        for log in logs:
            a = log.split(' ')
            if a[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        sorted_data = sorted(letter_logs, key=lambda x: x.split(' ', 1)[1])
        for data in sorted_data:
            answer.append(data)
        for data in digit_logs:
            answer.append(data)
        return answer

# 정답
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits