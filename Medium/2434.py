#2434. Using a Robot to Print the Lexicographically Smallest String
"""
    Time Complexity: O(n * 26)
    Space Complexity: O(n)
    
    Problem Overview: 
    - Given two operations:
        1. Move the first character from string 's' to string 't'.
        2. Move the last character from string 't' to the result.
    - Find the lexicographically smallest result string.

    Approach: Stack, Greedy
    - First In Last Out (FILO) -> Stack Pattern
    - Use a stack representing the characters moved from 's' to 't'
    - With each step, check the top of the stack with the smallest character in the rest of 's'
    - Keep adding the top of the stack to the result string until the top of the stack is not smaller than the smallest character in the rest of 's'.
    - Return the result string.
"""

class Solution:
    def robotWithString(self, s: str) -> str:
        res = ""
        stack = []
        ch = Counter(s)
        mn = "a"

        for i in s:
            stack.append(i)
            ch[i] -= 1

            while mn != "z" and ch[mn] == 0:
                mn = chr(ord(mn) + 1)
            
            while stack and stack[-1] <= mn:
                res += stack[-1]
                stack.pop()
        
        return res