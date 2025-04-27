        for i in range(2,len(nums)):
            if(nums[right_index] + nums[left_index]) == nums[equal_index] / 2:
                count += 1
                
            right_index += 1
            equal_index += 1
            left_index += 1