class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        sum_avgs = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]
        for i in range(m - 2):
            for j in range(n - 2):
                ok = True
                for di in range(3):
                    if not ok:
                        break
                    for dj in range(3):
                        if dj < 2:
                            if abs(image[i + di][j + dj] - image[i + di][j + dj + 1]) > threshold:
                                ok = False
                                break
                        if di < 2:
                            if abs(image[i + di][j + dj] - image[i + di + 1][j + dj]) > threshold:
                                ok = False
                                break
                if not ok:
                    continue
                s = 0
                for di in range(3):
                    for dj in range(3):
                        s += image[i + di][j + dj]
                avg = s // 9
                for di in range(3):
                    for dj in range(3):
                        sum_avgs[i + di][j + dj] += avg
                        cnt[i + di][j + dj] += 1
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if cnt[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] = sum_avgs[i][j] // cnt[i][j]
        return result