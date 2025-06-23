#2081. Sum of k-Mirror Numbers 
"""
    Time Complexity: O(sqrt(10^10))
    Space Complexity: O(1)
    
    Problem Overview: Sum all the number from 1 to n, that the number should be a palindrome when converted to base k. 

    Approach: Math, Enumerator
    - Instead of check all the number from 1 to n, we can generate half of the palindrome and then mirror it to get the full palindrome.
    - Then check if the number is a palindrome in base k.
    - Return the sum of all the k-mirror numbers. 
"""
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            for op in [0, 1]:
                for i in range(left, right):
                    if cnt == n:
                        break

                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            left = right

        return ans