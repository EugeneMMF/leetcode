from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        freq = Counter(nums)
        end_counts = defaultdict(int)

        for num in nums:
            if freq[num] == 0:
                continue

            freq[num] -= 1

            if end_counts[num - 1] > 0:
                end_counts[num - 1] -= 1
                end_counts[num] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                end_counts[num + 2] += 1
            else:
                return False
        
        return True
