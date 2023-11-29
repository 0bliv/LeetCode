class Solution(object):
    def isRobotBounded(self, instructions):
        x, y = 0, 0
        direction = 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = moves[direction]
                x += dx
                y += dy
            elif instruction == 'L':
                direction = (direction - 1) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4

        return (x, y) == (0, 0) or direction != 0
