class Solution:
    def totalFruit(self, fruits):
        left = 0
        counts = {}
        max_len = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] = counts.get(fruit, 0) + 1
            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
