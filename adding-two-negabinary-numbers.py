class Solution:
    def addNegabinary(self, arr1, arr2):
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += arr1[i]
                i -= 1
            if j >= 0:
                s += arr2[j]
                j -= 1
            res.append(s & 1)
            carry = -(s // 2)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
