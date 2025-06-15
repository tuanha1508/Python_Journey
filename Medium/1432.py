#1432. Max Difference You Can Get From Changing an Integer
"""
    Time Complexity: O(n) 
    Space Complexity: O(n)
    
    Problem Overview: In two operations : 
    - Change one digit of the number to any digit from 0 to 9.
    - Replace all occurrences of a digit with choosen digit.
    - Find the maximum difference between two numbers that can be obtained by performing the above operations.

    Approach: Math, Greedy
    - Convert the number to a string to easily manipulate its digits.
    - For the maximum number, replace the first non-9 digit with 9.
    - For the minimum number, replace the first non-0 digit with 0 (if it's not the first digit) or 1 (if it is the first digit).
    - Calculate the difference between the maximum and minimum numbers obtained.
"""

class Solution:
    def maxDiff(self, num: int) -> int:
        def change(x, y):
            return str(num).replace(str(x), str(y))

        min_num = max_num = num
        for x in range(10):
            for y in range(10):
                res = change(x, y)
                if res[0] != "0":
                    res_i = int(res)
                    min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)

        return max_num - min_num