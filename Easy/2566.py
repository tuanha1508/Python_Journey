# 2566. Minimum Difference by Remapping a Digit
"""
     Time Complexity: O(1)
    Space Complexity: O(1)
    
    Problem Overview: Change one digit in a number to maximize the difference between the maximum and minimum numbers.

    Approach: Greedy, Math
    - Greedy : maximum number is obtained by changing the first non-9 digit to 9 -> maximun value
    -          minimum number is obtained by changing the first non-minimum digit to 0 -> minimum value
    - Iterate through the digits of the number, find the first digit that is not 9 for maximum.
    - For minimum, find the first digit change.
    - Construct the maximum and minimum numbers by replacing the digits accordingly.
    - Finally, return the difference between the maximum and minimum numbers.
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], "9")
        t = t.replace(t[0], "0")
        return int(s) - int(t)