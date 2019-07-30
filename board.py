import numpy as np

def convert_position_to_coordinate(position, cols):
    x_axis = cols.index(position[0])
    y_axis = int( 10 if position[-1] == 0 else position[-1] ) -1 #int(position[1:2] if len(position) == 3 else position[1:3])
    return x_axis, y_axis

def map_out_potential_coordinates(position, direction, ship_length):
    x_axis = position[0]
    y_axis = int(position[-1] if len(position) == 2 else position[1:])
    potential_coordinates = [position]
    if direction == 'v':
        for i in range(ship_length - 1):
            potential_coordinates.append((x_axis + str(y_axis + i + 1)))
    if direction == 'h':
        for i in range(ship_length - 1):
            horizontal_columns = 'abcdefghij'
            potential_coordinates.append(
                (horizontal_columns[horizontal_columns.index(
                    x_axis) + i + 1]) + str(y_axis)
            )

    return potential_coordinates

class Board:
    def __init__(self, player_name, fleet_positions):

        self.player_name = player_name

        #top part
        self.tracker = np.zeros((10, 10), int)
        #tracker key :             # 0 blank            # 1 miss            # 2 hit             

        #?
        self.incoming_attacks = np.zeros((10, 10), int)    

        #bottom part
        self.ocean = np.zeros((10, 10), int)

        #fleet
        self.fleet_layout = self._setup_fleet(fleet_positions)

        #fleet in ocean
        self.cols = 'abcdefghij'
        self.ship_key = {'destroyer' : 1, 'sub' : 2, 'cruiser' : 3, 'battleship' : 4, 'carrier' : 5}
        self.ocean = self._fleet_in_ocean()



        # fleet_layout key
        # display Description  size
        # 0       Empty
        # 5       Carrier      (5)
        # 4       Battleship   (4)
        # 3       Cruiser      (3)
        # 2       Submarine    (3)
        # 1       Destroyer    (2)

    def _setup_fleet(self, fleet_positions) :

        #dict of ships 
        fleet = {}

        #Josh logic

        #example output:
        fleet = {
                'destroyer' : [ 'a1', 'a2' ],
                'sub' : [ 'b1', 'b2', 'b3' ],
                'cruiser' : [ 'c1', 'c2', 'c3' ],
                'battleship' : [ 'd1', 'd2', 'd3', 'd4' ],
                'carrier' : [ 'f10', 'g10', 'h10', 'i10', 'j10'] }

        return fleet


    def fleet_audit(self) :
        results = []
        hits = self.incoming_attacks * self.ocean

        for ship in self.fleet_layout : 
            results.append([ship])
            for i in self.fleet_layout[ship] :
                iy, ix = convert_position_to_coordinate(i, self.cols)

                results[-1].append( hits[ix][iy] if hits[ix][iy] == 0 else hits[ix][iy] )

        return results

    def progress(self) :
        sunkards = self.incoming_attacks * self.ocean
        flat = sunkards.flatten('C')
        nonzero = [x for x in flat if x > 0]
        count_hits = len(nonzero)
        return round(count_hits / 17 * 100,1)

    def _fleet_in_ocean(self) :
        #returns ocean part of the board with ships
        ocean_out = self.ocean.copy()

        for ship in self.fleet_layout :
            for i in self.fleet_layout[ship] :
                y, x = convert_position_to_coordinate(i, self.cols)
                ocean_out[x][y] = self.ship_key[ship]

        return ocean_out

    def __str__(self) :
        #col header
        out = '   | '
        for a in self.cols :
            out += a + ' | '

        out += '\n   -'

        for a in self.cols : out += '----'
        out += '\n'

        #Tracker
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

        #the fold in pysical gameboard
        for a in self.cols : out += '-----'
        out += '\n'


        #Ocean
        k = 1
        for i in self.ocean:
            if k < 10 : out += ' '
            out += str(k) + ' | '
            for j in i :
                if str(j) == '0' : out += '  | '
                #elif len([x for x in ]) > 0 : 
                else: 
                    out += str(j) + ' | '
            k += 1
            out += '\n'

        for a in self.cols  : out += '----'

        out += '----'

        return out
        