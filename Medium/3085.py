#3085. Minimum Deletions to Make String K-Special
"""
    Time Complexity: O(n + C^2)
    Space Complexity: O(n)
    
    Problem Overview: Make the difference between every pair of characters in the string at most k.

    Approach: Map, Count, Array, Brute Force
    - Try for each unique character in the string, calculate the number need to deletion if we choose frequency for this character is the minimum.
    - Find the minimum each trial.
    - Return the minimum result.
"""

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)

        for i in word:
            cnt[i] += 1

        res = len(word)

        for i in cnt.values():
            curr = 0
            for j in cnt.values():
                if i > j:
                    curr += j
                elif i + k < j:
                    curr += j - (i + k)
            res = min(res, curr)

        return res
