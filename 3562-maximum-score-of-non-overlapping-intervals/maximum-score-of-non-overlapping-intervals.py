from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [start, end, weight, original_index]
        arr = [
            [intervals[i][0], intervals[i][1], intervals[i][2], i]
            for i in range(n)
        ]

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose start > arr[i].end
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best (score, indices) from i onward
        # using at most k intervals
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: skip current interval
                skip_score, skip_ids = dp[i + 1][k]

                # Option 2: take current interval
                take_score, take_ids = dp[next_idx[i]][k - 1]

                take_score += arr[i][2]
                take_ids = take_ids + [arr[i][3]]

                # Keep indices sorted for lexicographical comparison
                take_ids.sort()

                # Choose better score
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_ids)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_ids)

                else:
                    # Same score -> lexicographically smaller indices
                    if take_ids < skip_ids:
                        dp[i][k] = (take_score, take_ids)
                    else:
                        dp[i][k] = (skip_score, skip_ids)

        return dp[0][4][1]