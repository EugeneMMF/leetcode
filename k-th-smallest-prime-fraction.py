class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)

        def check(mid_val: float) -> tuple[int, int, int]:
            count = 0
            max_frac_val = 0.0
            res_i = 0
            res_j = 1

            left = 0
            for right in range(1, n):
                while left < right and arr[left] / arr[right] <= mid_val:
                    if arr[left] / arr[right] > max_frac_val:
                        max_frac_val = arr[left] / arr[right]
                        res_i = arr[left]
                        res_j = arr[right]
                    left += 1
                count += left
            return count, res_i, res_j

        low = 0.0
        high = 1.0
        ans_num = 0
        ans_den = 1

        for _ in range(100):
            mid = (low + high) / 2
            
            count, current_ans_num, current_ans_den = check(mid)

            if count >= k:
                ans_num = current_ans_num
                ans_den = current_ans_den
                high = mid
            else:
                low = mid
        
        return [ans_num, ans_den]
