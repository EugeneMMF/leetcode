class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        while candies > 0:
            give = i + 1
            if give > candies:
                give = candies
            res[i % num_people] += give
            candies -= give
            i += 1
        return res
