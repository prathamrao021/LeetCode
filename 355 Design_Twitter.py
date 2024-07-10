import collections
class Twitter:
    def __init__(self):
        self.posts = collections.defaultdict(set)
        self.followings = collections.defaultdict(set)
        self.recent = []
 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].add(tweetId)
        self.recent.append(tweetId)

    def getNewsFeed(self, userId: int):
        check_set = set()

        for i in self.posts[userId]:
            check_set.add(i)

        ans = []
        
        for j in self.followings[userId]:
            for i in self.posts[j]:
                check_set.add(i)
        
        for i in self.recent[::-1]:
            if i in check_set:
                ans.append(i)
                if len(ans) == 10:
                    break
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == "__main__":
    t = Twitter()
    t.postTweet(1,5)
    t.getNewsFeed(1)
    t.follow(1,2)
    t.postTweet(2,6)
    t.getNewsFeed(1)
    t.unfollow(1,2)
    t.getNewsFeed(1)