class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed),reverse=True)
        fleet = 0
        mymax = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > mymax:
                fleet += 1
                mymax = time

        return fleet