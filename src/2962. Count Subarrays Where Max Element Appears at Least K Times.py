class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k <= 0:
            return 0
        
        M = max(nums)
        positions = [i for i, x in enumerate(nums) if x == M]
        
        m = len(positions)
        if m < k:
            return 0
        
        total = 0
        for i in range(m - k + 1):
            first_pos = positions[i]
            prev_pos  = positions[i-1] if i > 0 else -1
            kth_pos   = positions[i + k - 1]
            
            left_count = first_pos - prev_pos
            
            right_count = n - kth_pos
            
            total += left_count * right_count
        
        return total
