import typing
class Solution:
    def countMentions(self, numberOfUsers: int, events: typing.List[typing.List[str]]) -> typing.List[int]:
        next_online = [0] * numberOfUsers
        mentions = [0] * numberOfUsers
        processed = []
        for e in events:
            typ, ts_str, arg = e
            ts = int(ts_str)
            priority = 0 if typ == "OFFLINE" else 1
            processed.append((ts, priority, typ, arg))
        processed.sort()
        for ts, _, typ, arg in processed:
            if typ == "OFFLINE":
                uid = int(arg)
                next_online[uid] = ts + 60
            else:
                if arg == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif arg == "HERE":
                    for i in range(numberOfUsers):
                        if ts >= next_online[i]:
                            mentions[i] += 1
                else:
                    tokens = arg.split()
                    for tkn in tokens:
                        if tkn.startswith("id"):
                            uid = int(tkn[2:])
                            mentions[uid] += 1
        return mentions
