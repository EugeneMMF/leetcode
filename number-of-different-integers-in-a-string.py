class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        i = 0
        n = len(word)
        while i < n:
            if word[i].isdigit():
                start = i
                while i < n and word[i].isdigit():
                    i += 1
                num = word[start:i].lstrip('0')
                if num == '':
                    num = '0'
                nums.add(num)
            else:
                i += 1
        return len(nums)