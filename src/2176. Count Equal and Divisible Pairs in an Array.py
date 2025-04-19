import itertools

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = {}
        
        for i in range(len(nums)):
            if map.__contains__(nums[i]):
                map[nums[i]].append(i)
            else:
                new_list = []
                new_list.append(i)
                map[nums[i]] = new_list
        
        result = 0
        
        for key in map:
            value = map[key]
            if len(value) > 1:
                pares = list(itertools.combinations(map[key], 2))
                
                for par in pares:
                    if (par[0]*par[1]) % k == 0:
                        result += 1
                        
        return result
                
    
if __name__ == '__main__':
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))
    k = int(input("Enter value for k: "))
    
    # print(nums)
    sol = Solution()
    result = sol.countPairs(nums, k)
    print(f"Number of pairs (i,j) where nums[i] == nums[j] and (i*j) is divisible by {k}: {result}")