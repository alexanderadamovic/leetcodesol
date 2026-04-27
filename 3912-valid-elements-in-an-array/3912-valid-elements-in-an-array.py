class Solution(object):
    def findValidElements(self, nums):
        n = len(nums)
        
        prefix_max = [float('-inf')] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i-1])
        
        suffix_max = [float('-inf')] * n
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i+1])
        
        result = []
        for i in range(n):
            if i == 0 or i == n - 1:
                result.append(nums[i])
            elif nums[i] > prefix_max[i]:
                result.append(nums[i])
            elif nums[i] > suffix_max[i]:
                result.append(nums[i])
        
        return result
        