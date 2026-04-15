import math

def get_player_pos() -> tuple:
    valid_set = False
    while (valid_set is False):
        coords_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        acumulattor = ""
        coordinates = []
        for x in coords_input:
            if x == ',' and len(acumulattor) > 0:
                coordinates = coordinates + [acumulattor]
                acumulattor = ""
            else:
                acumulattor = acumulattor + x
        coordinates = coordinates + [acumulattor]
        acumulattor = ""
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        coords_tuple = ()
        coords_list = []
        error = False
        for i in coordinates:
            try:
                coords_list = coords_list + [float(i)]
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                error = True
                break
        if error is True:
            continue
        valid_set = True
    coords_tuple = (coords_list[0], coords_list[1], coords_list[2])
    return (coords_tuple)


def main() -> None:
    print("=== Game Coordinate System ===")
    print(f"Get a first set of coordinates")
    coords = get_player_pos()
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    first_set_distance = math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)
    print(f"Distance to center: {round(first_set_distance, 4)}\n")
    print(f"Get a second set of coordinates")
    second_coords = get_player_pos()
    final_distance = math.sqrt((second_coords[0] - coords[0])**2 + (second_coords[1] - coords[1])**2 + (second_coords[2] - coords[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(final_distance, 4)}")


if __name__ == "__main__":
	main()
