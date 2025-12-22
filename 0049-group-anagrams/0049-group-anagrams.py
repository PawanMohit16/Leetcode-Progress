class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        ans = {}

        for word in strs:
            mydict = {}
            for letter in word:
                if letter not in mydict:
                    mydict[letter] = 1
                else:
                    mydict[letter] += 1
            
            key = tuple(sorted(mydict.items()))                

            if key not in ans:
                ans[key] = [word]

            else:
                ans[key].append(word)

        return list(ans.values())