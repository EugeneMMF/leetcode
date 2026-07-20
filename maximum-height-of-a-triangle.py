class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        max_h = 0
        for h in range(1, 101):
            total = h * (h + 1) // 2
            if total > red + blue:
                break
            for start in (0, 1):
                r_used = 0
                b_used = 0
                for i in range(1, h + 1):
                    if (start ^ ((i - 1) & 1)) == 0:
                        r_used += i
                    else:
                        b_used += i
                if r_used <= red and b_used <= blue:
                    max_h = h
                    break
        return max_h