class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        count = 0
        for w in words:
            rev = w[::-1]
            if w in word_set and rev in word_set and w != rev:
                word_set.remove(w)
                word_set.remove(rev)
                count += 1
        return count
