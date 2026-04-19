class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        from collections import deque, Counter
        n = len(friends)
        visited = [False] * n
        q = deque([id])
        visited[id] = True
        cur = 0
        while q and cur < level:
            for _ in range(len(q)):
                u = q.popleft()
                for v in friends[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            cur += 1
        cnt = Counter()
        for u in q:
            for video in watchedVideos[u]:
                cnt[video] += 1
        sorted_videos = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        return [v for v, _ in sorted_videos]
