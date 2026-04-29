import math


def get_player_pos() -> tuple[float, float, float]:
    while (True):
        coords_input = input("Enter new coordinates "
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
    coords1 = get_player_pos()
    x1, y1, z1 = coords1
    print(f"Got a first tuple: {coords1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    first_set_distance = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(first_set_distance, 4)}\n")
    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    x2, y2, z2 = second_coords
    final_distance = math.sqrt((x2 - x1)**2
                               + (y2 - y1)**2
                               + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(final_distance, 4)}")


if __name__ == "__main__":
    main()
