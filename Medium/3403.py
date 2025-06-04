#3403. Find the Lexicographically Largest String From the Box I
"""
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Problem Overview: find the lexicographically larget string from the original string by split k string.

    Approach: String
    1. If numFriends is 1, return the original string.
    2. Compare all possible substrings of the original string as long as it the rest part still can split (k - 1) substrings.
    3. Return the largest substring found.

"""
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        for i in range(n):
            res = max(res, word[i : min(i + n - numFriends + 1, n)])
        return res