
class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        n = len(price)
        memo = {}

        # Filter out special offers that are more expensive than buying individually
        # This optimization can reduce the number of offers to check, but is not strictly necessary for correctness.
        # It's safer to keep all offers and let the recursion find the minimum.
        # However, for an offer like [1,1,0,100] when price=[1,1], buying individually is 2, so 100 is bad.
        # We can remove offers where the offer price is higher than buying the items individually.
        filtered_special = []
        for offer in special:
            offer_cost_individual = 0
            for i in range(n):
                offer_cost_individual += offer[i] * price[i]
            if offer[n] < offer_cost_individual:
                filtered_special.append(offer)

        # We also consider buying items individually as a base method.
        # The recursion explores all combinations of special offers and individual purchases.
        # The `calculate_cost` function will return the minimum price for a given `current_needs`.
        def calculate_cost(current_needs_tuple: tuple) -> int:
            if current_needs_tuple in memo:
                return memo[current_needs_tuple]

            # Convert tuple to list for easier manipulation
            current_needs = list(current_needs_tuple)

            # Option 1: Calculate the cost if all remaining items are bought individually
            min_current_cost = 0
            for i in range(n):
                min_current_cost += current_needs[i] * price[i]

            # Option 2: Try applying each special offer
            for offer in filtered_special: # Use filtered_special
                offer_price = offer[n]
                
                # Check if this offer can be applied without exceeding current needs
                can_apply = True
                next_needs = [0] * n
                for i in range(n):
                    if offer[i] > current_needs[i]:
                        can_apply = False
                        break
                    next_needs[i] = current_needs[i] - offer[i]
                
                if can_apply:
                    # If the offer can be applied, recursively find the cost for the remaining needs
                    # and add the current offer's price.
                    min_current_cost = min(min_current_cost, offer_price + calculate_cost(tuple(next_needs)))
            
            # Store the result in memoization table before returning
            memo[current_needs_tuple] = min_current_cost
            return min_current_cost

        # Start the recursion with the initial needs
        return calculate_cost(tuple(needs))

