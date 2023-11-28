# 오답
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = {}
        paragraph = re.sub("[!?,;.]", " ", paragraph)
        para = paragraph.split()
        for word in para:
            word = word.lower()
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for w in sorted_words:
            if w[0] in banned:
                pass
            else:
                return w[0]

# 정답
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # \w -> 단어문자, ^ -> not
    # 단어 문자가 아닌 모든 문자를 공백으로 치환
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]
    
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]