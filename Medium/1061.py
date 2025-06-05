#1061. Lexicographically Smallest Equivalent String
"""
    Time Complexity: O(n + m * 26)
    Space Complexity: O(n + 26)
    
    Problem Overview: 
    - Given two strings s1 and s2, and a string baseStr
    - Given that each character in s1 === each character in s2, mean that it can replact for each other
    - You need to find the lexicographically smallest equivalent string of baseStr

    Approach: DFS, Union-Find
    - Create initial graph with s1 and s2 that mean s1[i] can be replaced with s2[i] and vice versa
    - DFS all characters can replace with baseStr[i], find the smallest character
    - Append the smallest character to result string
    - Return the result string
"""
class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x == y: return 
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        G = UnionFind(26)
        n, m = len(s1), len(baseStr)
        for i in range(n):
            G.Union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        ans = ""
        for x in baseStr:
            ans += (chr(G.Find(ord(x) - 97) + 97))
        return ans
        