class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = [int(c) for c in boxes]
        n = len(arr)
        left_counts = [0] * n
        left_ops = [0] * n
        right_counts = [0] * n
        right_ops = [0] * n
        left_counts[0] = arr[0]
        for i in range(1, n):
            left_counts[i] = left_counts[i-1] + arr[i]
            left_ops[i] = left_ops[i-1] + left_counts[i-1]
        right_counts[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right_counts[i] = right_counts[i+1] + arr[i]
            right_ops[i] = right_ops[i+1] + right_counts[i+1]
        return [left_ops[i] + right_ops[i] for i in range(n)]
