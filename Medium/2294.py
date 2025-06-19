#2294. Partition Array Such That Maximum Difference Is K
"""
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Problem Overview: Divide array into n / 3 arrays such that maximum difference between any two elements in each array is at most k.

    Approach: Sort, Array
    - To minimize the maximum difference, sort the array and group elements in triplets.
    - If the difference between the first and last element of each triplet exceeds k, it is impossible in any ways to divide the array as required.
    - Return the triplets if all conditions are satisfied.
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cmp = nums[0]
        res = 1
        for i in nums:
            if i - cmp <= k:
                continue
            else:
                res += 1
            cmp = i
        return res
