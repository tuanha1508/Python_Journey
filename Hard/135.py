#135. Candy
"""
    Time Complexity: O(ratings.size())
    Space Complexity: O(ratings.size())
    
    Problem Overview: 
    - Distribute candies to children base on their rating such that :
        1. Each child must have at least one candy.
        2. Children with a higher rating get more candies than their neighbors with a lower rating.
    - Return the minimum number of candies you need to have to distribute to the children.
    
    Approach: Greedy, Array
    - Call an array dp, where dp[i] is the number of candies that child i will receive.
    - Because the current child will depend on the adjacent children, which means we just consider the left or right child. 
    - Then, we need to iterate the array twice: 
        1. From left to right, if the current child has a higher rating than the previous one, then it will receive one more candy than the previous child.
        2. From right to left, if the current child has a higher rating than the next one, then it will receive one more candy than the next child.
    - Must ensure that the current child get max from both iterations. It must be max to ensure that the current child has more candies than its neighbors with a lower rating.
    - Finally, sum all the candies in the dp array to get the result.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 0
        n = len(ratings) - 1
        dp = [1] * (n + 1)
        
        for i in range(1, n + 1):
            if ratings[i] < ratings[i - 1]:
                dp[i - 1] = dp[i] + 1
            elif ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        
        for i in range(n - 1, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
            elif ratings[i] < ratings[i + 1]:
                dp[i + 1] = max(dp[i + 1], dp[i] + 1)
        
        res = sum(dp)
        return res