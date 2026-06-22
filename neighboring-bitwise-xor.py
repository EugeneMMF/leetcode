class Solution:
    def doesValidArrayExist(self, derived):
        n = len(derived)
        if n == 1:
            return derived[0] == 0
        for start in (0, 1):
            o_prev = start
            valid = True
            for i in range(n - 1):
                o_next = o_prev ^ derived[i]
                o_prev = o_next
            if (o_prev ^ start) == derived[-1]:
                return True
        return False
