class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []

        for s, e in sorted(intervals):
            if not ans or ans[-1][1] < s:
                ans.append([s,e])


            else:
                ans[-1][1] = max(e, ans[-1][1])
        
        return ans
            

        