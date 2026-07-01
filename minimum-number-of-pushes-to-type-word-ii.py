class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        freq.sort(reverse=True)
        pushes = 0
        for i, f in enumerate(freq):
            if f == 0:
                break
            pushes += f * (i // 8 + 1)
        return pushes