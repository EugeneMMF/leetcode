class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = collections.defaultdict(set)
        for s in allowed:
            allowed_map[s[:2]].add(s[2])

        def solve(level):
            if len(level) == 1:
                return True

            next_level_candidates = []
            for i in range(len(level) - 1):
                possible_top_blocks = allowed_map[level[i:i+2]]
                if not possible_top_blocks:
                    return False
                next_level_candidates.append(list(possible_top_blocks))

            for combo in itertools.product(*next_level_candidates):
                if solve("".join(combo)):
                    return True
            return False

        return solve(bottom)

