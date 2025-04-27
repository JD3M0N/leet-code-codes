class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        
        right_index = 0
        equal_index = 1
        left_index = 2
        
        for i in range(2,len(nums)):
            if(nums[right_index] + nums[left_index]) * 2 == nums[equal_index] :
                count += 1
                
            right_index += 1
            equal_index += 1
            left_index += 1
            
        return count
    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.countSubarrays(nums)
    print(f"Number of subarrays: {result}")