class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0
        prefix_counts = {0: 1}
        
        for x in nums:
            curr_sum += x
            count += prefix_counts.get(curr_sum - k, 0)
            
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        
        return count
    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    k_input = int(input("Enter the target sum (k): "))
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.subarraySum(nums, k_input)
    print(f"Number of subarrays with sum {k_input}: {result}")