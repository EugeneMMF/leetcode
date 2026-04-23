class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        n = numCourses
        reach = [[False]*n for _ in range(n)]
        for a, b in prerequisites:
            reach[a][b] = True
        for k in range(n):
            rk = reach[k]
            for i in range(n):
                if reach[i][k]:
                    ri = reach[i]
                    for j in range(n):
                        if rk[j]:
                            ri[j] = True
        return [reach[u][v] for u, v in queries]
