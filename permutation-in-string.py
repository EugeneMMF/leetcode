class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        window_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1

        def matches(arr1, arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False
            return True

        if matches(s1_counts, window_counts):
            return True

        for i in range(n1, n2):
            window_counts[ord(s2[i]) - ord('a')] += 1
            window_counts[ord(s2[i - n1]) - ord('a')] -= 1

            if matches(s1_counts, window_counts):
                return True
        
        return False
