#2616. Minimize the Maximum Difference of Pairs
"""
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    
    Problem Overview: Minimize the maximum difference between p pairs of numbers in an array.

    Approach: Binary Search
    - Aware that two adjacent numbers after sorting result in the smaallest difference --> Sort the array.
    - Use the binary search with each mid value, compare and count how many pairs have a difference less than or equal to mid -> meaning that the maximum difference is mid.
    - If the number of pairs is greater than or equal to p, then we can try to minimize the maximum difference further by adjusting the right boundary.
    - If the number of pairs is less than p, we need to increase the minimum difference by adjusting the left boundary.
    - The process continues until the left boundary meets the right boundary, which will be the minimum maximum difference possible.
    - Return the left boundary as the result.
"""

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count = 0
            i = 1
            while i < n and count < p:
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            if count >= p:
                high = mid
            else:
                low = mid + 1
        return low