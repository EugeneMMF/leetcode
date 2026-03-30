class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        count = 0
        left = 0
        specials = []

        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                specials.append("1" + self.makeLargestSpecial(s[left + 1 : i]) + "0")
                left = i + 1

        specials.sort(reverse=True)
        return "".join(specials)

