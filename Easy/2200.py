#2200. Find All K-Distant Indices in an Array
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Problem Overview: find index that satisfy that |i - j| <= k where nums[j] == key, return all such indices.

    Approach: Array, Twopointer.
    - Iterate through the array, for each index i where nums[i] == key, calculate the range of indices that are k distant from i.
    - Use a variable to track the last added index to avoid duplicates.
    - Push all valid indices into the result vector.
    - Return the result vector.
"""
class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res