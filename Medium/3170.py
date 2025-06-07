#3170. Lexicographically Minimum String After Removing Stars
"""
    Time Complexity: O(n * 26)
    Space Complexity: O(n)
    
    Problem Overview:
    Given string s:
    - Remove all characters that are stars '*'.
    - For each character '*' removed, remove the smallest character on the left of the start. 
    - Return the lexicographically smallest string possible after all removals.

    Approach: Stack, String
    - We use a stack to keep track of the indices of characters in the string.
    - For each character in the string:
        - If it is not a star, we push its index onto the stack.
        - If it is a star, we pop the top of the stack (which gives us the index of the smallest character) and mark that position as a star.
    - Finally, we construct the result string by skipping all the stars.
"""

class Solution:
    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != "*":
                cnt[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = "*"
                        break
        return "".join(c for c in arr if c != "*")
