class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            wordMap[tuple(count)].append(w)
        return list(wordMap.values())