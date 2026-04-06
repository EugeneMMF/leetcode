import collections

class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # Find initial positions of the player, box, and target
        player_start = (-1, -1)
        box_start = (-1, -1)
        target = (-1, -1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'S':
                    player_start = (r, c)
                elif grid[r][c] == 'B':
                    box_start = (r, c)
                elif grid[r][c] == 'T':
                    target = (r, c)
        
        # Directions for movement: (dr, dc) for Up, Down, Left, Right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # dist[box_r][box_c][player_r][player_c] stores the minimum number of pushes
        # to get the box to (box_r, box_c) and the player to (player_r, player_c).
        # Initialize with -1 to indicate unvisited states.
        dist = [[[[ -1 for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(m)]

        # Deque for a 0-1 BFS. 0-cost moves (player movement) are added to the front,
        # 1-cost moves (box pushes) are added to the back.
        q = collections.deque()

        # Helper function to check if the player can reach a 'target_player_pos'
        # from their 'current_player_pos' while the box remains fixed at 'fixed_box_pos'.
        # Walls ('#') and the fixed box are obstacles for the player.
        def can_reach(current_player_r, current_player_c, target_player_r, target_player_c, fixed_box_r, fixed_box_c):
            # The target player position must be within grid bounds and not a wall.
            if not (0 <= target_player_r < m and 0 <= target_player_c < n and grid[target_player_r][target_player_c] != '#'):
                return False

            # If the player is already at the target position, it's reachable.
            if (current_player_r, current_player_c) == (target_player_r, target_player_c):
                return True

            q_reach = collections.deque()
            q_reach.append((current_player_r, current_player_c))
            visited_reach = set([(current_player_r, current_player_c)])

            while q_reach:
                r, c = q_reach.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds and if the cell has been visited in this sub-BFS
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited_reach:
                        # Player cannot move through walls ('#') or the fixed box's current position
                        if grid[nr][nc] != '#' and (nr, nc) != (fixed_box_r, fixed_box_c):
                            if (nr, nc) == (target_player_r, target_player_c):
                                return True # Target reached
                            visited_reach.add((nr, nc))
                            q_reach.append((nr, nc))
            return False # Target not reachable

        # Initialize BFS with the starting state: box at box_start, player at player_start, 0 pushes.
        dist[box_start[0]][box_start[1]][player_start[0]][player_start[1]] = 0
        q.append((box_start[0], box_start[1], player_start[0], player_start[1]))

        while q:
            curr_br, curr_bc, curr_pr, curr_pc = q.popleft()
            current_pushes = dist[curr_br][curr_bc][curr_pr][curr_pc]

            # If the box is already at the target, no further pushes are needed for this path
            # (although other player positions might lead to fewer overall pushes)
            # In a 0-1 BFS, when a state is popped, we have found the minimum cost to reach it.
            # So, if box is at target, this `current_pushes` is the minimal pushes for this
            # specific final player position. We will find the overall minimum at the end.

            # Try to push the box in all four directions
            for i in range(4):
                dr, dc = dirs[i]

                # Calculate the potential new position of the box
                next_box_r, next_box_c = curr_br + dr, curr_bc + dc
                # Calculate the position the player needs to be at to push the box
                # from (curr_br, curr_bc) to (next_box_r, next_box_c).
                # The player must be on the opposite side of the push direction.
                player_to_push_r, player_to_push_c = curr_br - dr, curr_bc - dc

                # Check if the potential new box position is valid (within bounds and not a wall)
                if not (0 <= next_box_r < m and 0 <= next_box_c < n and grid[next_box_r][next_box_c] != '#'):
                    continue # Cannot push box into a wall or out of bounds

                # Check if the player can reach the required position to push the box,
                # given the box is currently at (curr_br, curr_bc).
                if can_reach(curr_pr, curr_pc, player_to_push_r, player_to_push_c, curr_br, curr_bc):
                    # If the player can reach the push position, perform the push.
                    # The player's new position will be where the box used to be.
                    new_player_r, new_player_c = curr_br, curr_bc
                    new_pushes = current_pushes + 1

                    # If this new state (box_pos, player_pos) has not been visited yet,
                    # or we found a path to it with fewer pushes, update and add to queue.
                    if dist[next_box_r][next_box_c][new_player_r][new_player_c] == -1 or \
                       new_pushes < dist[next_box_r][next_box_c][new_player_r][new_player_c]:
                        
                        dist[next_box_r][next_box_c][new_player_r][new_player_c] = new_pushes
                        # This is a 1-cost transition (a push), so add to the back of the deque.
                        q.append((next_box_r, next_box_c, new_player_r, new_player_c))
        
        # After the BFS completes, iterate through all possible player positions
        # for the target box position to find the overall minimum pushes.
        ans = float('inf')
        for r in range(m):
            for c in range(n):
                if dist[target[0]][target[1]][r][c] != -1:
                    ans = min(ans, dist[target[0]][target[1]][r][c])

        # If 'ans' is still infinity, it means the target was unreachable.
        return ans if ans != float('inf') else -1

