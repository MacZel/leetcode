class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_map = { 'U': [1,0], 'D': [-1,0], 'L': [0,-1], 'R': [0,1]}
        starting_pos = [0,0]
        for move in moves:
            starting_pos[0] += move_map[move][0]
            starting_pos[1] += move_map[move][1]
        if starting_pos == [0,0]:
            return True
        else:
            return False
