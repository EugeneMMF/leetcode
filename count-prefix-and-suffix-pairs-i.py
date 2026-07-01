class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            a = words[i]
            for j in range(i + 1, len(words)):
                b = words[j]
                if b.startswith(a) and b.endswith(a):
                    count += 1
        return count
