class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list) 
        for i, word in enumerate(strs):
            char = [0] * 26
            for c in word:
                num = ord(c) - ord('a')
                char[num] += 1
            wordMap[tuple(char)].append(word)
        return list(wordMap.values())