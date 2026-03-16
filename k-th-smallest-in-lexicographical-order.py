class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(curr: int, n: int) -> int:
            count = 0
            first = curr
            last = curr + 1
            while first <= n:
                count += min(n + 1, last) - first
                first *= 10
                last *= 10
            return count

        current = 1
        k -= 1  # Adjust k to be 0-indexed offset from 'current'

        while k > 0:
            steps = countSteps(current, n)
            if k >= steps:
                # The k-th number is not in the subtree rooted at 'current'.
                # Skip this whole branch and move to the next sibling.
                k -= steps
                current += 1
            else:
                # The k-th number is in the subtree rooted at 'current'.
                # Go down to the first child.
                current *= 10
                k -= 1 # We've "passed" 'current' itself to consider its children.
        
        return current
