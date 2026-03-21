import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total_elements = m * n
        self.available_count = self.total_elements
        self.mapping = {} # Stores logical_index -> physical_index mappings

    def flip(self) -> list[int]:
        # 1. Pick a random logical index from the currently available range [0, self.available_count - 1]
        rand_logical_idx = random.randrange(self.available_count)

        # 2. Get the actual physical index that corresponds to this logical index.
        # If rand_logical_idx is in the mapping, it means it was previously swapped
        # to point to a different physical index. Otherwise, it points to itself.
        flipped_physical_idx = self.mapping.get(rand_logical_idx, rand_logical_idx)

        # 3. Decrement the count of available elements.
        # This new self.available_count is the size of the range for the *next* flip.
        # The logical index for the element that was at the end of the range is now self.available_count.
        self.available_count -= 1
        
        # 4. To maintain contiguity in the logical index space [0, self.available_count - 1],
        # we move the element that was at the *last* logical position into the chosen `rand_logical_idx`'s slot.
        # The logical index of the last available element *before* decrementing `self.available_count` was `self.available_count`.
        # So we need to fetch the physical value that this `self.available_count` (the new value) maps to.
        # If `self.available_count` (the new value) itself was a key in `mapping`, it means it points to some
        # physical index. Otherwise, it points to itself.
        # The `pop` method allows us to get the value and remove the key in one step.
        val_from_last_slot = self.mapping.pop(self.available_count, self.available_count)
        
        # Update the mapping: the chosen `rand_logical_idx` now points to the physical index
        # that was previously at the end of the available range.
        self.mapping[rand_logical_idx] = val_from_last_slot
        
        # 5. Convert the flipped physical index back to (i, j) coordinates
        r = flipped_physical_idx
        i = r // self.n
        j = r % self.n
        
        return [i, j]

    def reset(self) -> None:
        # Reset the count of available elements to the total number of cells.
        self.available_count = self.total_elements
        # Clear the mapping, as all cells are now '0' again.
        self.mapping = {}

