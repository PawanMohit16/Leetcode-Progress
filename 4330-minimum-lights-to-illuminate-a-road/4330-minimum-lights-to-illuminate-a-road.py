class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        arr = [False] * n
        m = 0
        for i in range(n):
            if m > 0:
                arr[i] = True
            m = max(lights[i], m-1)
        m = 0
        for i in range(n-1,-1,-1):
            if m > 0 or lights[i] > 0:
                arr[i] = True
            m = max(lights[i], m-1)


        ans = 0
        curr = 0
        for i in range(n):
                              
            if not arr[i]: 
                curr += 1

            else:
                ans +=  (curr+ 2) // 3
                curr = 0

        ans +=  (curr+ 2) // 3

        return ans
                
                
                