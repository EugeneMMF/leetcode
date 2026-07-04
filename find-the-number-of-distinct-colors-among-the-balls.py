class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_count = {}
        distinct = 0
        result = []
        for x, y in queries:
            old = ball_color.get(x)
            if old is not None:
                cnt = color_count[old] - 1
                if cnt == 0:
                    del color_count[old]
                    distinct -= 1
                else:
                    color_count[old] = cnt
            ball_color[x] = y
            cnt = color_count.get(y, 0) + 1
            if cnt == 1:
                distinct += 1
            color_count[y] = cnt
            result.append(distinct)
        return result
