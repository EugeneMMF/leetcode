class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        from bisect import bisect_right
        tails = []
        ans = []
        for h in obstacles:
            pos = bisect_right(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
            ans.append(pos + 1)
        return ans