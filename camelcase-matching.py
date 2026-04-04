class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def check(query: str, pattern_str: str) -> bool:
            p_idx = 0
            q_idx = 0

            while q_idx < len(query):
                if p_idx < len(pattern_str) and query[q_idx] == pattern_str[p_idx]:
                    p_idx += 1
                    q_idx += 1
                elif query[q_idx].islower():
                    q_idx += 1
                else:
                    return False

            return p_idx == len(pattern_str)

        answer = []
        for query_item in queries:
            answer.append(check(query_item, pattern))
        
        return answer
