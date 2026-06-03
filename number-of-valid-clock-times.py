class Solution:
    def countTime(self, time: str) -> int:
        count = 0
        for h in range(24):
            hh = f"{h:02d}"
            for m in range(60):
                mm = f"{m:02d}"
                cand = f"{hh}:{mm}"
                match = True
                for i in range(5):
                    if time[i] != '?' and time[i] != cand[i]:
                        match = False
                        break
                if match:
                    count += 1
        return count