class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
       
        left, right = 0, len(arr) - 1
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= mid:
                
                first_true_index = mid
                right = mid - 1
            else:
                
                left = mid + 1

        
        if first_true_index != -1 and arr[first_true_index] == first_true_index:
            return first_true_index
        return -1

        