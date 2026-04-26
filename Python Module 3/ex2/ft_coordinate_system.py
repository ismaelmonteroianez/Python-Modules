import math


def get_player_pos() -> tuple[float, float, float]:
    while (True):
        coords_input = input("Enter new coordinates"
                             "as floats in format 'x,y,z': ")
        coordinates = coords_input.split(',')
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        coords_list = []
        error = False
        for i in coordinates:
            try:
                coords_list.append(float(i))
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                error = True
                break
        if error:
            continue
        return (coords_list[0], coords_list[1], coords_list[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coords = get_player_pos()
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    first_set_distance = math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)
    print(f"Distance to center: {round(first_set_distance, 4)}\n")
    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    final_distance = math.sqrt((second_coords[0] - coords[0])**2
                               + (second_coords[1] - coords[1])**2
                               + (second_coords[2] - coords[2])**2)
    print(f"Distance between the 2 sets of coordinates:"
          f"{round(final_distance, 4)}")


if __name__ == "__main__":
    main()
