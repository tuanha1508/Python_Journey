#2138. Divide a String Into Groups of Size k
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Problem Overview: Distribute string into groups of size k, if the last group is not full, fill it with a given character.

    Approach: String
    - Calculate to know if the last group is full or not.
    - Add the fill character into initial string until the size if a multiple of k
    - Use substr to get each group of size k.
    - Return the result.
"""

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [] 
        n = len(s)
        curr = 0
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        res[-1] += fill * (k - len(res[-1]))
        return res