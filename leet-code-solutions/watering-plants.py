class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        x = 0

        for i, plant in enumerate(plants):
            if x + plant <= capacity:
                x += plant
            else:
                x = plant 
                ans += i * 2

        return ans + len(plants)

            