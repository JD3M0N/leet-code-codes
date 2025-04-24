class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        distinct_in_array = set()
         
        for i in range(len(nums)):
            distinct_in_array.add(nums[i])
            
        target = len(distinct_in_array)
        
        
        for start in range(len(nums)):
            tempSet = set()
            
            for end in range(start, len(nums)):
                tempSet.add(nums[end])
                if len(tempSet) == target:
                    count += 1    
                    
        return count
    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))

    # print(nums)
    sol = Solution()
    result = sol.countCompleteSubarrays(nums)
    print(f"Number of subarrays: {result}")