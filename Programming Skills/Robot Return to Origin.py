class Solution(object):
    def judgeCircle(self, moves):
        count_U = moves.count('U')
        count_D = moves.count('D')
        count_L = moves.count('L')
        count_R = moves.count('R')

        return count_U == count_D and count_L == count_R