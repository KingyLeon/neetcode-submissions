class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for i, word in enumerate(strs):
            wordCount = Counter(word)
            key = tuple(sorted(wordCount.items()))
            wordMap[key].append(word)
        returnValue = [words for item, words in wordMap.items()]
        return returnValue
