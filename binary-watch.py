class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []

        for h_leds in range(max(0, turnedOn - 6), min(5, turnedOn + 1)):
            m_leds = turnedOn - h_leds

            hours_list = []
            for h in range(12):
                if bin(h).count('1') == h_leds:
                    hours_list.append(h)

            minutes_list = []
            for m in range(60):
                if bin(m).count('1') == m_leds:
                    minutes_list.append(m)
            
            for h_val in hours_list:
                for m_val in minutes_list:
                    res.append(f"{h_val}:{m_val:02d}")

        return res
