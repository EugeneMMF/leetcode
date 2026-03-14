class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = False
        has_upper = False
        has_digit = False
        for char in password:
            if 'a' <= char <= 'z':
                has_lower = True
            elif 'A' <= char <= 'Z':
                has_upper = True
            elif '0' <= char <= '9':
                has_digit = True

        missing_types = 0
        if not has_lower:
            missing_types += 1
        if not has_upper:
            missing_types += 1
        if not has_digit:
            missing_types += 1

        total_replacements_for_repeats = 0
        repeats_mod_0 = []
        repeats_mod_1 = []
        repeats_mod_2 = []

        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                total_replacements_for_repeats += length // 3
                if length % 3 == 0:
                    repeats_mod_0.append(length)
                elif length % 3 == 1:
                    repeats_mod_1.append(length)
                else:
                    repeats_mod_2.append(length)
            i = j

        steps = 0

        if n < 6:
            insertions_needed = 6 - n
            steps += insertions_needed
            missing_types = max(0, missing_types - insertions_needed)
            steps += missing_types
            return steps

        elif n <= 20:
            steps = max(missing_types, total_replacements_for_repeats)
            return steps

        else:
            deletions_needed = n - 20
            steps += deletions_needed

            for length in repeats_mod_0:
                if deletions_needed > 0:
                    total_replacements_for_repeats -= 1
                    deletions_needed -= 1

            for length in repeats_mod_1:
                if deletions_needed >= 2:
                    total_replacements_for_repeats -= 1
                    deletions_needed -= 2
            
            total_replacements_for_repeats -= (deletions_needed // 3)

            steps += max(missing_types, total_replacements_for_repeats)
            return steps
