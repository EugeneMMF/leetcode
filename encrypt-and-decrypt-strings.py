class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.key_to_val = {k: v for k, v in zip(keys, values)}
        self.enc_counts = {}
        for w in dictionary:
            enc = []
            valid = True
            for ch in w:
                if ch not in self.key_to_val:
                    valid = False
                    break
                enc.append(self.key_to_val[ch])
            if valid:
                enc_str = ''.join(enc)
                self.enc_counts[enc_str] = self.enc_counts.get(enc_str, 0) + 1

    def encrypt(self, word1: str) -> str:
        res = []
        for ch in word1:
            val = self.key_to_val.get(ch)
            if val is None:
                return ""
            res.append(val)
        return ''.join(res)

    def decrypt(self, word2: str) -> int:
        return self.enc_counts.get(word2, 0)

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
