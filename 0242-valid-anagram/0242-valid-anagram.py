class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mymap = {}

        for letter in s:
            if letter not in mymap:
                mymap[letter] = 1
            else:
                mymap[letter] += 1

        mymap2 = {}

        for letter in t:
            if letter not in mymap2:
                mymap2[letter] = 1
            else:
                mymap2[letter] += 1

        print(mymap)
        print(mymap2)

        return mymap == mymap2