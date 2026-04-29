class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                res.append('G')
                i += 1
            elif command[i] == '(':
                if i + 1 < n and command[i+1] == ')':
                    res.append('o')
                    i += 2
                else:
                    res.append('al')
                    i += 4
        return ''.join(res)
