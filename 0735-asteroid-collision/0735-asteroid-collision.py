from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        space = []

        for rock in asteroids:
            while space and space[-1] > 0 and rock < 0:
                if abs(rock) > space[-1]:
                    space.pop()
                elif abs(rock) == space[-1]:
                    space.pop()
                    break
                else:
                    break
            else:
                space.append(rock)

        return space
