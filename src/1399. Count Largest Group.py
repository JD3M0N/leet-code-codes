class Solution(object):
    
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        map = {}
        
        maxim = 0
        
        for i in range(1, n+1):
            sum = self.digit_sum(i)
            if map.__contains__(sum):
                map[sum] += 1
                maxim = max(maxim, map[sum])
            else :
                map[sum] = 1
                if maxim < 1 :
                    maxim = 1
        
        newMax = 0
        
        for key in map :
            if map[key] == maxim :
                newMax += 1

        return newMax
            
    def digit_sum(self, n):
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total
    
if __name__ == '__main__':
    n = int(input("Enter value for n: "))
    
    sol = Solution()
    result = sol.countLargestGroup(n)
    print(f"Minimum number of groups: {result}")