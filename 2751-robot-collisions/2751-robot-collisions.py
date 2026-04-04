class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        items = []
        stack = []
        n = len(positions)
        
        for i in range(n):
            items.append([positions[i], i, healths[i], directions[i]])
        items.sort()

        for i in range(n):
            if stack:
                while stack and stack[-1][-1] == 'R' and items[i][-1] == 'L':
                    if stack[-1][1] == items[i][2]:
                        stack.pop()
                        items[i][2] = 0
                        break
                    elif items[i][2] > stack[-1][1]:
                        items[i][2] -= 1
                        stack.pop()
                    else:
                        stack[-1][1] -= 1
                        items[i][2] = 0
                        break

                    
                if items[i][2] > 0:
                    stack.append([items[i][1], items[i][2], items[i][-1]])
            else:
                stack.append([items[i][1], items[i][2], items[i][-1]])

        res = []
        stack.sort()  # sorts by original index

        res = []
        for i, j, k in stack:
            res.append(j)

        return res

