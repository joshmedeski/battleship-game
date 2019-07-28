import numpy as np


# def convert_position_to_coordinate(position):
#     x_axis = 'abcdefghij'.index(position[0])
#     y_axis = 1 - (position[1:2] if len(position) == 3 else position[1:3])
#     return x_axis, y_axis

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


print(map_out_potential_coordinates('a8', 'v', 3))
print(map_out_potential_coordinates('a8', 'h', 3))


class Board:
    def __init__(self, player_name, fleet_positions):
        self.player_name = player_name
        self.tracker = np.zeros((10, 10), int)
        self.fleet_layout = self._setup_fleet(fleet_positions)
