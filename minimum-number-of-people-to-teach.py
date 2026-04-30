class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = [set(l) for l in languages]
        bad_users = set()
        for u, v in friendships:
            if not (user_langs[u - 1] & user_langs[v - 1]):
                bad_users.add(u)
                bad_users.add(v)
        if not bad_users:
            return 0
        min_teach = len(bad_users)
        for lang in range(1, n + 1):
            teach = sum(1 for u in bad_users if lang not in user_langs[u - 1])
            if teach < min_teach:
                min_teach = teach
        return min_teach
