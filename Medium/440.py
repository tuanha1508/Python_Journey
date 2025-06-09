#440. K-th Smallest in Lexicographical Order
"""
    Time Complexity: O(log(n)^2)
    Space Complexity: O(1)
    
    Problem Overview: Given two integers n and k, return the k_th lexicographically smallest integer in the range [1, n].

    Approach: Trie
    - Initialize curr to 1 (current prefix) and decrement k by 1.

    - While k is greater than 0:

        + Calculate the number of steps in the subtree rooted at curr using countSteps(n, curr, curr + 1).
        + If the number of steps is less than or equal to k:
        + Increment curr by 1 to move to the next prefix.
        + Decrement k by the number of skipped steps (i.e., k -= step).
        + Otherwise:
        + Multiply curr by 10 to move to the next level in the tree (i.e., curr *= 10).
        + Decrement k by 1 to account for the current level.
        + Return the value of curr as the k-th smallest number in lexicographical order.

    - countSteps function:
        + Initialize steps to 0 to keep track of the count of numbers in the range.
        + While prefix1 is less than or equal to n:
        + Add the number of integers between prefix1 and prefix2 to steps using steps += Math.min(n + 1, prefix2) - prefix1. This ensures the count does not exceed n by capping prefix2 at n + 1 if prefix2 is larger than n.
        + Multiply prefix1 and prefix2 by 10 to move to the next level in the tree.
        + Return the total number of steps counted.
"""
class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1

        return curr

    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps