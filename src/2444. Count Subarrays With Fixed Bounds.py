class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        count = 0
        lastInvalid = -1
        lastMin = -1
        lastMax = -1
        
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                lastInvalid = i
            
            if x == minK:
                lastMin = i
            if x == maxK:
                lastMax = i
            
            j = min(lastMin, lastMax)
            if j > lastInvalid:
                count += (j - lastInvalid)
        
        return count


if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    minK_input = int(input("Enter the minimum value (minK): "))
    maxK_input = int(input("Enter the maximum value (maxK): "))
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.countSubarrays(nums, minK_input, maxK_input)
    print(f"Number of subarrays with bounds [{minK_input}, {maxK_input}]: {result}")