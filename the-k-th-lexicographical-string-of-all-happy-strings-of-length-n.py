class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.k = k
        self.result = ""
        def dfs(prefix):
            if len(prefix) == n:
                self.k -= 1
                if self.k == 0:
                    self.result = prefix
                    return True
                return False
            for ch in "abc":
                if not prefix or prefix[-1] != ch:
                    if dfs(prefix + ch):
                        return True
            return False
        dfs("")
        return self.result
