class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hashmap = {}

        for num in barcodes:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1


        print(hashmap)
        item, freq = zip(*sorted(hashmap.items(), reverse=True, key=lambda x: x[1]))

        items = list(item)
        freqs = list(freq)
        n = len(items)
        
        ans = [0] * len(barcodes)
        idx = 0

        for i in range(n):
            for j in range(freqs[i]):
                ans[idx] = items[i]
                idx += 2
                if idx >= len(barcodes):
                    idx = 1

        return ans