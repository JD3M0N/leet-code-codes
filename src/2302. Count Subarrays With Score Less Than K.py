class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        left = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while left <= right and curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            
            count += (right - left + 1)
        
        return count

if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    k_input = int(input("Enter the divisor (k): "))
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.countSubarrays(nums, k_input)
    print(f"Number of subarrays with score less than {k_input}: {result}")