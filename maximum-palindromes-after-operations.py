class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        total_chars = 0
        for w in words:
            total_chars += len(w)
        total_pairs = 0
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            total_pairs += words.count(ch)  # wrong, need counts across all words

        # correct approach: count all letters
        from collections import Counter
        counter = Counter()
        for w in words:
            counter.update(w)
        total_pairs = sum(v // 2 for v in counter.values())
        total_singles = total_chars - 2 * total_pairs

        req = []
        for w in words:
            L = len(w)
            req.append((L // 2, L % 2))
        req.sort(key=lambda x: x[0])
        count = 0
        for pairs_needed, odd_needed in req:
            if total_pairs < pairs_needed:
                break
            total_pairs -= pairs_needed
            if odd_needed:
                if total_singles > 0:
                    total_singles -= 1
                elif total_pairs > 0:
                    total_pairs -= 1
                    total_singles += 2
                    total_singles -= 1
                else:
                    break
            count += 1
        return count
