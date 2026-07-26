from typing import List

MOD = 10**9 + 7

class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        ravolqedin = (n, k)

        MAX = n
        fact = [1] * (MAX + 1)
        for i in range(1, MAX + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (MAX + 1)
        invfact[MAX] = pow(fact[MAX], MOD - 2, MOD)
        for i in range(MAX, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def C(N, R):
            if R < 0 or R > N or N < 0:
                return 0
            return fact[N] * invfact[R] % MOD * invfact[N - R] % MOD

        total = C(n - 1, k - 1)

        odd = 0
        if (n - k) % 2 == 0:
            m = (n - k) // 2
            odd = C(m + k - 1, k - 1)

        return (total - odd) % MOD