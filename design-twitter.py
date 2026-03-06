from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followers[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        self.followers[userId].add(userId)

        followed_users = self.followers[userId]

        all_relevant_tweets = []
        for followee_id in followed_users:
            all_relevant_tweets.extend(self.tweets[followee_id])

        all_relevant_tweets.sort(key=lambda x: x[0], reverse=True)

        news_feed = []
        for i in range(min(10, len(all_relevant_tweets))):
            news_feed.append(all_relevant_tweets[i][1])

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)

