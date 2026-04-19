class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        filtered=[]
        for id_, rating, vegan, price, dist in restaurants:
            if veganFriendly and not vegan:
                continue
            if price>maxPrice or dist>maxDistance:
                continue
            filtered.append((-rating, -id_, id_))
        filtered.sort()
        return [item[2] for item in filtered]
