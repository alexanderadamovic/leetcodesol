from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def dfs(i: int) -> int:
            
            ans = 1
            
            
            for j in range(i - 1, max(i - d - 1, -1), -1):
                
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))
                
            
            for j in range(i + 1, min(i + d + 1, n)):
                
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))
                
            return ans

       
        return max(dfs(i) for i in range(n))   