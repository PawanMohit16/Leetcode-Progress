class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr2 = list(range(1, len(arr)+k+1))
        for i in range(len(arr2)):
            if arr2[i] not in arr:
                k -= 1
                if k == 0:
                    return arr2[i] 
    
        
            
