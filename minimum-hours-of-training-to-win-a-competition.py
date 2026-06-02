from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0
        curr_energy = initialEnergy
        curr_exp = initialExperience
        for e, exp in zip(energy, experience):
            if curr_energy <= e:
                need = e - curr_energy + 1
                hours += need
                curr_energy += need
            if curr_exp <= exp:
                need = exp - curr_exp + 1
                hours += need
                curr_exp += need
            curr_energy -= e
            curr_exp += exp
        return hours
