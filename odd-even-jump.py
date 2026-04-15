class Solution:
    def oddEvenJumps(self, arr):
        n = len(arr)
        next_higher = [-1] * n
        next_lower = [-1] * n
        stack = []
        for _, i in sorted((val, idx) for idx, val in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        stack.clear()
        for _, i in sorted((-val, idx) for idx, val in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        good_odd = [False] * n
        good_even = [False] * n
        good_odd[-1] = good_even[-1] = True
        for i in range(n - 2, -1, -1):
            if next_higher[i] != -1:
                good_odd[i] = good_even[next_higher[i]]
            if next_lower[i] != -1:
                good_even[i] = good_odd[next_lower[i]]
        return sum(good_odd)
