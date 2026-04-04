class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):

        robots = sorted(zip(positions, range(len(positions)), healths, directions))
        stack = []

        for pos, idx, health, direction in robots:

            while stack and stack[-1][2] == 'R' and direction == 'L':
                top_idx, top_health, top_dir = stack[-1]

                if top_health == health:
                    stack.pop()
                    health = 0
                    break
                elif health > top_health:
                    health -= 1
                    stack.pop()
                else:
                    stack[-1][1] -= 1
                    health = 0
                    break

            if health > 0:
                stack.append([idx, health, direction])

        stack.sort()
        return [h for _, h, _ in stack]