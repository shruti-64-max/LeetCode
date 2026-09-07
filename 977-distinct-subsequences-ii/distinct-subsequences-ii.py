class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:
            new = dp

            if ch in last:
                new -= last[ch]

            last[ch] = dp
            dp = (dp + new) % MOD

        return (dp - 1) % MOD