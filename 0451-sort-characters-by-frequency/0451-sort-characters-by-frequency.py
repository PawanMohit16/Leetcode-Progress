class Solution:
    def frequencySort(self, s: str) -> str:
        
        hashmap = {}

        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1


        return "".join(k * v for k, v in sorted(hashmap.items(), reverse=True, key=lambda x: x[1]))

