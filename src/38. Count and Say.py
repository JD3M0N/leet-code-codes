class Solution(object):
    def RLE(self, s):
        
        current = s[0]
        amount = 1
        
        ans = []
        
        if len(s) == 1:
            ans.append("1")
            ans.append("1")
            
            answer = "".join(ans)
        
            return answer
        
        
        for i in s[1:]:
            if i == current :
                amount += 1
            else:
                ans.append(str(amount))
                ans.append(current)
                current = i
                amount = 1
                
        ans.append(str(amount))
        ans.append(current)          
                    
        # map = {}
        
        # for i in range (len(s)):
        #     if map.__contains__(s[i]):
        #         map[s[i]] += 1
        #     else:
        #         map[s[i]] = 1
        
        # ans = []
        
        # for key in map:
        #     ans.append(str(map[key]))
        #     ans.append(key)
        
        answer = "".join(ans)
        
        return answer
                
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        
        for i in range(n-1):
            ans = self.RLE(ans)
        
        return ans
    

if __name__ == '__main__':
    s = int(input("Ingresa n: "))
    sol = Solution()
    result = sol.countAndSay(s)
    print("La cadena es:", result) 