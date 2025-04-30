class Solution(object):
    def countSubarrays(self, k):
        """
        :type k: int
        :rtype: int
        """
        string = str(k)
        count = len(string)
        
        return count

if __name__ == '__main__':
    k_input = int(input("(k)"))

    sol = Solution()
    result = sol.countSubarrays(k_input)
    print(f"{result}")