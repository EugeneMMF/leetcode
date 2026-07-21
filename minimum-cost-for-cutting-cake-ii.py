class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        i = j = 0
        hPieces = 1
        vPieces = 1
        total = 0
        while i < len(horizontalCut) and j < len(verticalCut):
            if horizontalCut[i] > verticalCut[j]:
                total += horizontalCut[i] * vPieces
                hPieces += 1
                i += 1
            else:
                total += verticalCut[j] * hPieces
                vPieces += 1
                j += 1
        while i < len(horizontalCut):
            total += horizontalCut[i] * vPieces
            i += 1
        while j < len(verticalCut):
            total += verticalCut[j] * hPieces
            j += 1
        return total