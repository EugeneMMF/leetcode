import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        char_counts = collections.Counter(s)
        digit_counts = [0] * 10
        
        digit_counts[0] = char_counts['z']
        digit_counts[2] = char_counts['w']
        digit_counts[4] = char_counts['u']
        digit_counts[6] = char_counts['x']
        digit_counts[8] = char_counts['g']
        
        digit_counts[3] = char_counts['h'] - digit_counts[8]
        digit_counts[5] = char_counts['f'] - digit_counts[4]
        digit_counts[7] = char_counts['s'] - digit_counts[6]
        
        digit_counts[1] = char_counts['o'] - digit_counts[0] - digit_counts[2] - digit_counts[4]
        digit_counts[9] = char_counts['i'] - digit_counts[5] - digit_counts[6] - digit_counts[8]
        
        result_list = []
        for i in range(10):
            result_list.append(str(i) * digit_counts[i])
            
        return "".join(result_list)
