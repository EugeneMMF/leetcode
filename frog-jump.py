class Solution:
    def canCross(self, stones: list[int]) -> bool:
        # Create a dictionary to store stone positions and the set of possible jump sizes to reach them.
        # This acts as our DP table: stone_map[stone_pos] = {set of jump_sizes}
        stone_map = {stone: set() for stone in stones}

        # Initialize the first stone. The frog is initially on the first stone (position 0).
        # We represent this as having "jumped" 0 units to be on it.
        # The first *actual* jump from this stone must be 1 unit.
        stone_map[0].add(0)

        # Iterate through each stone in the sorted list of stones
        for current_stone_pos in stones:
            # For each jump size 'k' that allowed the frog to land on the current stone
            for last_jump_units in stone_map[current_stone_pos]:
                # If it's the initial state (last_jump_units == 0), the first jump must be 1 unit.
                if last_jump_units == 0:
                    next_jump_units = 1
                    next_stone_pos = current_stone_pos + next_jump_units
                    # Check if the next stone position exists in our map
                    if next_stone_pos in stone_map:
                        stone_map[next_stone_pos].add(next_jump_units)
                else:
                    # For any subsequent jump, the next jump can be k-1, k, or k+1 units.
                    for next_jump_units in [last_jump_units - 1, last_jump_units, last_jump_units + 1]:
                        # A jump must be at least 1 unit and in the forward direction.
                        if next_jump_units > 0:
                            next_stone_pos = current_stone_pos + next_jump_units
                            # Check if the next stone position exists in our map
                            if next_stone_pos in stone_map:
                                stone_map[next_stone_pos].add(next_jump_units)
            
        # After processing all stones, check if the last stone can be reached.
        # If the set of jump sizes for the last stone is not empty, it means it's reachable.
        return len(stone_map[stones[-1]]) > 0

