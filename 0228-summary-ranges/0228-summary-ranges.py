class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return []

        n = len(nums)
        
        prev = nums[0]
        next = nums[0]
        for i in range(1,n):
            if next + 1 == nums[i]:
                next = nums[i]

            else:
                if next != prev:
                    res.append(str(prev) + '->' + str(next))

                else:
                    res.append(str(prev))

                prev = nums[i]
                next = nums[i]

            
        if prev == next:
            res.append(str(prev))
        else:
            res.append(str(prev) + '->' + str(next))


                

        return res