class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        posdir = 0
        negdir = 0

        i = start
        while i != destination:
            posdir += distance[i]
            i = (i + 1) % n

        i = start
        while i != destination:
            i = (i - 1 + n) % n
            negdir += distance[i]

        return min(posdir, negdir)