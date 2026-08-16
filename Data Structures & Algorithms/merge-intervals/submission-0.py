class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        mp = defaultdict(int)

        for i, j in intervals:
            mp[i] += 1
            mp[j] -= 1

        res = []
        interval = []
        have = 0

        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]

            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res
        