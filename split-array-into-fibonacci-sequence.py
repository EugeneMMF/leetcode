class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        ans = []

        def backtrack(index):
            if index == n:
                return len(ans) >= 3

            for i in range(index, n):
                if num[index] == '0' and i > index:
                    break

                current_num = int(num[index:i+1])
                if current_num >= 2**31:
                    break

                if len(ans) < 2 or current_num == ans[-1] + ans[-2]:
                    ans.append(current_num)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) >= 2 and current_num > ans[-1] + ans[-2]:
                    break
            return False

        backtrack(0)
        return ans

