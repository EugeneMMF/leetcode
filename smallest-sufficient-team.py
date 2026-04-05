class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n_skills = len(req_skills)
        n_people = len(people)

        skill_to_int = {skill: i for i, skill in enumerate(req_skills)}

        people_skill_masks = []
        for person_skills_list in people:
            mask = 0
            for skill in person_skills_list:
                mask |= (1 << skill_to_int[skill])
            people_skill_masks.append(mask)

        def count_set_bits(n):
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        dp = [ (1 << n_people) - 1 ] * (1 << n_skills)
        dp[0] = 0

        for p_idx in range(n_people):
            person_skills_mask = people_skill_masks[p_idx]
            if person_skills_mask == 0:
                continue

            for current_skill_mask in range(1 << n_skills):
                if dp[current_skill_mask] == ((1 << n_people) - 1) and current_skill_mask != 0:
                    continue

                new_skill_mask = current_skill_mask | person_skills_mask
                candidate_new_team_mask = dp[current_skill_mask] | (1 << p_idx)

                if count_set_bits(candidate_new_team_mask) < count_set_bits(dp[new_skill_mask]):
                    dp[new_skill_mask] = candidate_new_team_mask
        
        final_person_mask = dp[(1 << n_skills) - 1]
        
        result_team_indices = []
        for i in range(n_people):
            if (final_person_mask >> i) & 1:
                result_team_indices.append(i)
        
        return result_team_indices
