class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True

        def crossProduct(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

        for i in range(2, len(coordinates)):
            if crossProduct(coordinates[0], coordinates[1], coordinates[i]) != 0:
                return False

        return True
