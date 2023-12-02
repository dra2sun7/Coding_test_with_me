class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []
        answer = []
        for str in strs:
            if sorted(str) in sorted_str:
                answer[sorted_str.index(sorted(str))].append(str)
            else:
                sorted_str.append(sorted(str))
                answer.append([str])
        return answer

# 다른 풀이
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())