class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned_s_chars = []
        for char in s:
            if char != '-':
                cleaned_s_chars.append(char.upper())
        cleaned_s = "".join(cleaned_s_chars)

        if not cleaned_s:
            return ""

        result_parts = []
        current_group_chars = []
        
        for i in range(len(cleaned_s) - 1, -1, -1):
            current_group_chars.append(cleaned_s[i])
            
            if len(current_group_chars) == k:
                current_group_chars.reverse() 
                result_parts.append("".join(current_group_chars))
                current_group_chars = []

        if current_group_chars:
            current_group_chars.reverse() 
            result_parts.append("".join(current_group_chars))
        
        result_parts.reverse()
        
        return "-".join(result_parts)
