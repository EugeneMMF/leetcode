class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n
        for i, v in enumerate(colsum):
            if v == 2:
                top[i] = bottom[i] = 1
                upper -= 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for i, v in enumerate(colsum):
            if v == 1:
                if upper > 0:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return []
        return [top, bottom]
