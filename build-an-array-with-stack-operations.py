class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        idx = 0
        for i in range(1, n + 1):
            if idx >= len(target):
                break
            if target[idx] == i:
                ops.append("Push")
                idx += 1
            else:
                ops.append("Push")
                ops.append("Pop")
        return ops
