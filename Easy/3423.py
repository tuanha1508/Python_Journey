#3423. Maximum Difference Between Adjacent Elements in a Circular Array
"""
    Time Complexity: O(n * Sigma^2)
    Space Complexity: O(1)
    
    Problem Overview: find the maximum difference between the odd frequency and even frequency in substrings have size of at least 'k'

    Approach :

    - Enumerate all pairs of characters `a` and `b` (digits 0-4) where `a` ≠ `b` to find optimal odd/even frequency combination
    - Use two-pointer technique with `left` and `right` pointers to explore all valid substrings of length ≥ `k`
    - Track counts `cnt_a`, `cnt_b` for current substring and `prev_a`, `prev_b` for prefix up to `left` pointer
    - Encode parity states as 2-bit numbers: `(count_a % 2) << 1 | (count_b % 2)` for efficient state management
    - Maintain `best[]` array storing minimum `prev_a - prev_b` values for each of the 4 possible parity states
    - Advance `left` pointer only when substring length ≥ `k` and `b` appears even times (≥ 2 occurrences)
    - Update `best[left_status]` with current `prev_a - prev_b` before moving `left` pointer forward
    - For each `right` position, calculate answer using target state `10` (odd `a`, even `b`) via XOR operation
    - Compute difference `(cnt_a - cnt_b) - best[right_status ^ 0b10]` to maximize odd-even frequency difference
    - Return maximum difference found across all character pairs and valid substring positions
"""

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = abs(nums[n - 1] - nums[0])

        for i in range(1, n):
            res = max(res, abs(nums[i] - nums[i - 1]))
        
        return res