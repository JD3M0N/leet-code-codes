class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        count = 0
        
        y = lower + differences[0]
        
        base = []
        
        base.append(lower)
        base.append(y)
        
        lowest = min(lower, y)
        biggest = max(lower,y)
        
        for i in range(1, len(differences)):
            base.append(differences[i] + base[i])
            
            lowest = min(lowest, base[i+1])
            biggest = max(biggest, base[i+1])
        
        minDistance = lower - lowest
        
        # if minDistance > 0 :
        #     for i in range (len(base)):
        #         base[i] += minDistance    
        
        minDistance = upper - (biggest + minDistance)
        
        if minDistance < 0 :
            return 0
        
        return minDistance + 1

if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))
    lower = int(input("Enter value for lower: "))
    upper = int(input("Enter value for upper: "))
    
    # print(nums)
    sol = Solution()
    result = sol.numberOfArrays(nums, lower, upper)
    print(f"Number of arrays: {result}")