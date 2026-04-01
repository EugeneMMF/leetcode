class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            parts = s.split('@')
            name = parts[0]
            domain = parts[1]
            masked_name = name[0] + "*****" + name[-1]
            return masked_name + "@" + domain
        else:
            digits_only = []
            for char in s:
                if char.isdigit():
                    digits_only.append(char)
            
            cleaned_digits = "".join(digits_only)
            
            num_digits = len(cleaned_digits)
            country_code_length = num_digits - 10
            
            local_number_suffix = cleaned_digits[-4:]
            
            if country_code_length == 0:
                return "***-***-" + local_number_suffix
            elif country_code_length == 1:
                return "+*-***-***-" + local_number_suffix
            elif country_code_length == 2:
                return "+**-***-***-" + local_number_suffix
            elif country_code_length == 3:
                return "+***-***-***-" + local_number_suffix
