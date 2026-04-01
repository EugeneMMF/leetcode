
class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        
        valid_replacements = []
        for i in range(len(indices)):
            idx = indices[i]
            src = sources[i]
            tgt = targets[i]
            
            if s[idx : idx + len(src)] == src:
                valid_replacements.append((idx, len(src), tgt))
        
        valid_replacements.sort()
        
        result_parts = []
        current_s_index = 0
        
        for idx, src_len, tgt in valid_replacements:
            result_parts.append(s[current_s_index : idx])
            result_parts.append(tgt)
            current_s_index = idx + src_len
            
        result_parts.append(s[current_s_index:])
        
        return "".join(result_parts)
