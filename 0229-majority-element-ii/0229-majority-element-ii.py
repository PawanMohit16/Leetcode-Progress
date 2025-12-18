class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        mydict = {}

        for i in nums:
            if i not in mydict:
                mydict[i] = 1

            else:
                mydict[i] += 1
        
        print(mydict)

        res = []
        threshold = len(nums) // 3
        for key in mydict.keys():
            if mydict[key] > threshold:
                res.append(key)

        return res
        