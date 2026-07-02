class Solution:
    def resultArray(self, nums):
        import bisect
        arr1, arr2 = [], []
        sorted1, sorted2 = [], []
        for i, val in enumerate(nums, start=1):
            if i == 1:
                arr1.append(val)
                bisect.insort(sorted1, val)
            elif i == 2:
                arr2.append(val)
                bisect.insort(sorted2, val)
            else:
                c1 = len(sorted1) - bisect.bisect_right(sorted1, val)
                c2 = len(sorted2) - bisect.bisect_right(sorted2, val)
                if c1 > c2:
                    arr1.append(val)
                    bisect.insort(sorted1, val)
                elif c1 < c2:
                    arr2.append(val)
                    bisect.insort(sorted2, val)
                else:
                    if len(arr1) < len(arr2):
                        arr1.append(val)
                        bisect.insort(sorted1, val)
                    elif len(arr1) > len(arr2):
                        arr2.append(val)
                        bisect.insort(sorted2, val)
                    else:
                        arr1.append(val)
                        bisect.insort(sorted1, val)
        return arr1 + arr2