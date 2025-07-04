#386. Lexicographical Numbers
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Problem Overview: Return all the integers in the range [1, n] sorted in lexicographical order.

    Approach: Implementation
    - We will generate all the numbers from 1 to n:
        - Start with the smallest number, 1.
        - Multiply by 10 until it exceeds n.
        - If the current number ends with a 9 or exceeds n, divide by 10 and increment.
    For example :
    Input: n = 5
    Step 1 - Start with 1
    Step 2 - Multiply by 10, now curr = 10 (exceeds n)
    Step 3 - Divide by 10, now curr = 1
    Step 4 - Increment, now curr = 2
    Step 5 - Repeat until all numbers are generated.
    - Store all generated numbers in a vector and return it.
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        curr = 1

        for _ in range(n):
            ans.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1

        return ans