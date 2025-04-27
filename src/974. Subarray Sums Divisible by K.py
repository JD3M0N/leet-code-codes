class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_mod_counts = {0: 1}  
        curr_sum = 0
        
        for x in nums:
            curr_sum = (curr_sum + x) % k
            count += prefix_mod_counts.get(curr_sum, 0)
            prefix_mod_counts[curr_sum] = prefix_mod_counts.get(curr_sum, 0) + 1
        
        return count


if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    k_input = int(input("Enter the divisor (k): "))
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.subarraysDivByK(nums, k_input)
    print(f"Number of subarrays divisible by {k_input}: {result}")