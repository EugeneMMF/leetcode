class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        children = [{}]
        cnt = [0]
        ans = 0
        for w in words:
            n = len(w)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and w[i] != w[j]:
                    j = pi[j - 1]
                if w[i] == w[j]:
                    j += 1
                pi[i] = j
            borders = set()
            l = n
            while l > 0:
                borders.add(l)
                l = pi[l - 1]
            node = 0
            for i, ch in enumerate(w, 1):
                if ch not in children[node]:
                    children[node][ch] = len(children)
                    children.append({})
                    cnt.append(0)
                node = children[node][ch]
                if i in borders:
                    ans += cnt[node]
            cnt[node] += 1
        return ans
