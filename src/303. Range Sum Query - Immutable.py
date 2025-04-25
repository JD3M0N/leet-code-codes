class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = []
        temp = 0
        
        for i in nums:
            temp += i
            self.sum.append(temp)
            

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > 0 and right > 0:
            return self.sum[right] - self.sum[left-1]
        else:
            return self.sum[left or right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)