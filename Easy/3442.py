#3442. Maximum Difference Between Even and Odd Frequency I
"""
    Time Complexity: O(s.size())
    Space Complexity: O(26)
    
    Problem Overview: Find the max odd frequency and min even frequency of characters in the string.

    Approach: Array, String
    - Count the frequency of each character in the string.
    - Track the maximum odd frequency and minimum even frequency.
    - Return the difference between the maximum odd frequency and minimum even frequency.
"""
class Solution:
    def maxDifference(self, s: str) -> int:
        m = [0] * 26
        odd = 1
        even = 102
        for i in s:
            m[ord(i) - ord('a')] += 1

        for i in m:
            if i & 1:
                odd = max(odd, i)
            elif i != 0:
                even = min(even, i)

        return odd - even
