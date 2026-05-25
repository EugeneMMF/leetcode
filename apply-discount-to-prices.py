class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        factor = (100 - discount) / 100
        for i, w in enumerate(words):
            if w and w[0] == '$' and w[1:].isdigit():
                price = int(w[1:])
                discounted = price * factor
                words[i] = f"${discounted:.2f}"
        return ' '.join(words)
