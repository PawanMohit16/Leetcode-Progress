from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int):

        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:

            if followee in self.tweets:

                index = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][index]

                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        res = []

        while heap and len(res) < 10:

            time, tweetId, followee, index = heapq.heappop(heap)

            res.append(tweetId)

            if index >= 0:

                nextTime, nextTweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (nextTime, nextTweetId, followee, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId != followerId:
            self.following[followerId].discard(followeeId)