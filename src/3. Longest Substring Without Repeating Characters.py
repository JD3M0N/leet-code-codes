class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max = 0
        current = 0
        begin = 0
        
        map = {}
        
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= begin:
                temp = map[s[i]]
                map[s[i]] = i
                max = max if max > current else current
                current = i - temp
                begin = temp + 1
            else :
                map[s[i]] = i
                current += 1
        
        max = max if max > current else current
        
        return max


if __name__ == '__main__':
    s = input("Ingresa un string: ")
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print("El número de la mayor subcadena sin repetir caracteres es:", result)