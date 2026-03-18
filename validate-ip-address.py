class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def is_ipv4(ip_str):
            parts = ip_str.split('.')
            if len(parts) != 4:
                return False
            
            for part in parts:
                # 1. Check if part is empty.
                # This handles cases like "1.1..1" or ".1.1.1" or "1.1.1.1." where an empty segment might occur.
                if not part:
                    return False
                
                # 2. Check for leading zeros, unless the part itself is "0".
                if len(part) > 1 and part[0] == '0':
                    return False
                
                # 3. Check if all characters are digits.
                if not part.isdigit():
                    return False
                
                # 4. Convert to integer and check if the value is within range [0, 255].
                num = int(part)
                if not (0 <= num <= 255):
                    return False
            
            return True

        def is_ipv6(ip_str):
            parts = ip_str.split(':')
            if len(parts) != 8:
                return False
            
            # Valid hexadecimal characters
            hex_digits = "0123456789abcdefABCDEF"
            
            for part in parts:
                # 1. Check the length of the part (1 to 4 characters).
                if not (1 <= len(part) <= 4):
                    return False
                
                # 2. Check if all characters in the part are valid hexadecimal digits.
                for char in part:
                    if char not in hex_digits:
                        return False
            
            return True

        # Determine if the IP string potentially contains IPv4 or IPv6 separators
        if '.' in queryIP:
            if is_ipv4(queryIP):
                return "IPv4"
        elif ':' in queryIP:
            if is_ipv6(queryIP):
                return "IPv6"
        
        # If neither separator is found or validation fails, it's "Neither"
        return "Neither"

