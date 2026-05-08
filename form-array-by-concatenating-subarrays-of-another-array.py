class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(groups)
        starts = []
        for g in groups:
            m = len(g)
            cur = []
            for i in range(len(nums)-m+1):
                if nums[i:i+m] == g:
                    cur.append(i)
            starts.append(cur)
        prev_ends = {-1}
        for idx in range(n):
            cur_ends = set()
            for prev_end in prev_ends:
                for s in starts[idx]:
                    if s > prev_end:
                        cur_ends.add(s + len(groups[idx]) - 1)
            if not cur_ends:
                return False
            prev_ends = cur_ends
        return True
