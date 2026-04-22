class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        # max number
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = int(s)
        # min number
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch not in ('0', '1'):
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = int(s)
        return max_num - min_num
