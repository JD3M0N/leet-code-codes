class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        map = {}
        
        for i in range(len(answers)):
            if map.__contains__(answers[i]):
                map[answers[i]] += 1
            else:
                map[answers[i]] = 1
        
        ans = 0
        
        for key in map:
            if key + 1 == map[key]:
                ans += max(map[key], key + 1)
            else :
                if key >= map[key]:
                    ans += key + 1
                else :
                    if key != 0 and key != 1:
                        ans += map[key]
                        ans += abs((map[key] % (key + 1)) - (key + 1))
                    if key == 0 :
                        ans += map[key]
                    if key == 1 :
                        if map[key] % 2 == 0:
                            ans += map[key]
                        else :
                            ans += map[key] + 1
                    
                    
        return ans
                

if __name__ == '__main__':
    nums_input = input("Enter the answer of the rabbits separated by spaces: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.numRabbits(nums)
    print(f"Minimum number of rabbits: {result}")