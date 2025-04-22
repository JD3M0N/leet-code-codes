class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9 + 7

        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a-b] % MOD

        prev = [1] * (maxValue + 1)
        totalChains = [0] * (n + 1)
        totalChains[1] = maxValue

        maxK = n  
        for k in range(2, n + 1):
            curr = [0] * (maxValue + 1)
            tot = 0
            for d in range(1, maxValue + 1):
                cnt = prev[d]
                if cnt:
                    multiple = 2*d
                    while multiple <= maxValue:
                        curr[multiple] = (curr[multiple] + cnt) % MOD
                        multiple += d
            tot = sum(curr) % MOD
            if tot == 0:
                break
            totalChains[k] = tot
            prev = curr

        ans = 0
        for k in range(1, n + 1):
            if totalChains[k] == 0:
                break
            ways = comb(n-1, k-1)
            ans = (ans + totalChains[k] * ways) % MOD

        return ans
