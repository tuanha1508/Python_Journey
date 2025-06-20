#3443. Maximum Manhattan Distance After K Changes
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Problem Overview: Find the maximum Manhattan distance after making at most k changes to the string s, where each change can replace a character with any of 'N', 'S', 'E', or 'W'.

    Approach: Greedy, Array
    - At each step, efficient change that we change min(k, i) characters and result in distance can gain 2 * k or i + 1 - distance. 
    - Keep track of the counts of 'N', 'S', 'E', and 'W' as we iterate through the string.
    - Calculate the current Manhattan distance and update the result accordingly.
    - Return the maximum distance found.
"""
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        north = south = west = east = 0
        for i in range(len(s)):
            if s[i] == 'N':
                north += 1
            if s[i] == 'S':
                south += 1
            if s[i] == 'W':
                west += 1
            if s[i] == 'E':
                east += 1

            curr = abs(north - south) + abs(west - east)
            res = max(res, curr + min(2 * k, i + 1 - curr))
        
        return res