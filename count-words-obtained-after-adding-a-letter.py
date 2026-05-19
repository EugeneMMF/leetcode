class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_masks = set()
        for w in startWords:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            start_masks.add(mask)
        count = 0
        for w in targetWords:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            for i in range(26):
                if mask & (1 << i):
                    prev = mask ^ (1 << i)
                    if prev in start_masks:
                        count += 1
                        break
        return count
