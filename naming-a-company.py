class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = {}
        for word in ideas:
            groups.setdefault(word[0], set()).add(word[1:])
        letters = list(groups.keys())
        ans = 0
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a, b = letters[i], letters[j]
                sa, sb = groups[a], groups[b]
                ca = sum(1 for s in sa if s not in sb)
                cb = sum(1 for s in sb if s not in sa)
                ans += ca * cb * 2
        return ans
