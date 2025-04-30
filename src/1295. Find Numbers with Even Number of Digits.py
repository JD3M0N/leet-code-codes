class Solution(object):    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        
        for i in range(len(nums)):
            temp = str(nums[i])
            parity = len(temp)
            if parity % 2 == 0:
                count += 1
        
        return count
    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.findNumbers(nums)
    print(f"Number of even numbers: {result}")