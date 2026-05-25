class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        has_lower = has_upper = has_digit = has_special = False
        specials = set("!@#$%^&*()-+")
        prev = ''
        for ch in password:
            if ch == prev:
                return False
            prev = ch
            if 'a' <= ch <= 'z':
                has_lower = True
            elif 'A' <= ch <= 'Z':
                has_upper = True
            elif '0' <= ch <= '9':
                has_digit = True
            elif ch in specials:
                has_special = True
        return has_lower and has_upper and has_digit and has_special