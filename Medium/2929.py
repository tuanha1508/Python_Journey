#2929. Distribute Candies Among Children II
"""
    Time Complexity: O(min(n, limit))
    Space Complexity: O(1)
    
    Problem Overview: Find how many ways to distribute n candies to 3 children, each children must have >= limit candies.

    Approach: Math, Brute Force 
    - Call a + b + c = n, where a, b, c are candies given to each child.
    - If we give child A candies, then we can split (n - a) candies between child B and C.
    - As each child must have at least 'limit' candies, so the amount of candies B and C get should be at least 2 * limit or (n - a) >= (2 * limit)
    - Iterate loop from [0, min(limit, n)] to try all possible values of a.
    - For each value of a, we check if (n - a) >= (2 * limit), if true then we can calculate the number of ways to distribute the remaining candies.
"""
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            if n <= i + 2 * limit:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res