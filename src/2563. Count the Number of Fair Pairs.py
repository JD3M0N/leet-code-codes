from itertools import combinations

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        
        def countLE(target):
            count = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
            return count
        
        return countLE(upper) - countLE(lower - 1)
                    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))
    lower = int(input("Enter value for lower: "))
    upper = int(input("Enter value for upper: "))
    
    # print(nums)
    sol = Solution()
    result = sol.countFairPairs(nums, lower, upper)
    print(f"Number of pairs fair pairs: {result}")