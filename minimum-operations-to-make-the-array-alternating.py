from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        even = nums[0::2]
        odd = nums[1::2]
        if not odd:
            return 0
        cnt_even = Counter(even)
        cnt_odd = Counter(odd)
        top_even = cnt_even.most_common(2)
        top_odd = cnt_odd.most_common(2)
        val_even1, cnt_even1 = top_even[0]
        val_odd1, cnt_odd1 = top_odd[0]
        if val_even1 != val_odd1:
            return (len(even) - cnt_even1) + (len(odd) - cnt_odd1)
        cnt_even2 = top_even[1][1] if len(top_even) > 1 else 0
        cnt_odd2 = top_odd[1][1] if len(top_odd) > 1 else 0
        return min((len(even) - cnt_even2) + (len(odd) - cnt_odd1),
                   (len(even) - cnt_even1) + (len(odd) - cnt_odd2))