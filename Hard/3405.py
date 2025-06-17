#3405. Count the Number of Arrays with K Matching Adjacent Elements
"""
    Time Complexity: O(k * log MOD
    Space Complexity: O(1)
    
    Problem Overview: Given n, m, and k :
    - find number of arrays of length n with elements from 1 to m that :
      + have exactly k pairs of adjacent elements that are equal.
    Approach: Math, Combinatorics, Inverse Modulo
"""

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod, d = 10 ** 9 + 7, n - 1
        if k > d:       
            return 0
        r, C = k, 1
        if r > d - r:   
            r = d - r
        if r:
            inv = [0] * (r + 1)
            inv[1] = 1
            for i in range(2, r + 1):
                inv[i] = mod - (mod // i) * inv[mod % i] % mod
            for i in range(1, r + 1):
                C = C * (d - r + i) % mod * inv[i] % mod
        return m * C % mod * pow(m - 1, d - k, mod) % mod

