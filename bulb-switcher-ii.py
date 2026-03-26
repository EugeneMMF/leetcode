
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        def calculate_bulb_state(a, e, o, f, num_bulbs):
            state = []
            for i in range(1, min(num_bulbs, 6) + 1):
                current_bulb_is_off = 0
                
                if a:
                    current_bulb_is_off ^= 1
                
                if i % 2 == 0 and e:
                    current_bulb_is_off ^= 1
                
                if i % 2 == 1 and o:
                    current_bulb_is_off ^= 1
                
                if i % 3 == 1 and f:
                    current_bulb_is_off ^= 1
                
                state.append(current_bulb_is_off)
            return tuple(state)

        possible_states = set()

        for a in range(2):
            for e in range(2):
                for o in range(2):
                    for f in range(2):
                        effective_press_count = a + e + o + f

                        if effective_press_count <= presses and \
                           (presses - effective_press_count) % 2 == 0:
                            possible_states.add(calculate_bulb_state(a, e, o, f, n))
        
        return len(possible_states)
