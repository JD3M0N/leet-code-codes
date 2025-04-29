class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        count_mod = defaultdict(int)
        count_mod[0] = 1
        
        curr_pref = 0
        result = 0
        
        for x in nums:
            if x % modulo == k:
                curr_pref = (curr_pref + 1) % modulo
            
            need = (curr_pref - k) % modulo
            result += count_mod[need]
            
            count_mod[curr_pref] += 1
        
        return result
