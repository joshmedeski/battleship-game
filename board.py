import numpy as np


class Board:
    def __init__(self):
        # self.fleet_layout = np.zeros((10, 10), int)
        self.cols = 'abcdefghij'
        
        self.tracker = np.zeros((10, 10), int)
        self.fleet_layout = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 4, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 4, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 4, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 4, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 5, 5, 5, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

# key
# 0 Empty
# 5 Carrier    (5)
# 4 Battleship (4)
# 3 Cruiser    (3)
# 2 Submarine  (3)
# 1 Destroyer  (2)

# 0 blank
# 1 miss
# 2 hit

# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 1 0 1 0 0 0
# 0 0 0 1 2 2 2 2 2 0
# 0 0 0 0 0 0 0 0 0 0

    def progress(self) :
        sunkards = game_board.tracker * game_board.fleet_layout
        flat = sunkards.flatten('C')
        nonzero = [x for x in flat if x > 0]
        count_hits = len(nonzero)
        return round(count_hits / 17 * 100,1)


    def __str__(self) :
        #col header
        out = '   | '
        for a in self.cols :
            out += a + ' | '
            
        out += '\n   -'
        
        for a in self.cols : out += '----'
        out += '\n'
        
        #row index
        k = 1
        for i in self.tracker :
            if k < 10 : out += ' ' + str(k) + ' | '; 
            else : out += str(k) + ' | '
            
            for j in i : 
                if str(j) == '0' : out += '  | '
                else: 
                    out +=  str(j) + ' | '
            k += 1
            out += '\n'
            
        
        for a in self.cols : out += '-----'
        out += '\n'
        
        k = 1
        for i in self.fleet_layout :
            if k < 10 : out += ' '
            out += str(k) + ' | '
            for j in i :
                if str(j) == '0' : out += '  | '
                else: 
                    out += str(j) + ' | '
            k += 1
            out += '\n'
            
        return out