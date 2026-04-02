class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        unique_signatures = set()

        for word in words:
            even_indexed_chars = []
            odd_indexed_chars = []
            
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even_indexed_chars.append(char)
                else:
                    odd_indexed_chars.append(char)
            
            signature_tuple = (
                "".join(sorted(even_indexed_chars)),
                "".join(sorted(odd_indexed_chars))
            )
            unique_signatures.add(signature_tuple)
        
        return len(unique_signatures)
