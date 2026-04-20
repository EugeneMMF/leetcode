class TweetCounts:
    def __init__(self):
        self.store = {}
    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.store:
            self.store[tweetName] = []
        self.store[tweetName].append(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        size = 60 if freq == "minute" else 3600 if freq == "hour" else 86400
        chunks = (endTime - startTime) // size + 1
        res = [0] * chunks
        if tweetName not in self.store:
            return res
        for t in self.store[tweetName]:
            if startTime <= t <= endTime:
                idx = (t - startTime) // size
                res[idx] += 1
        return res
