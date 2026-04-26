import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for args in sys.argv[1:]:
        item_data = args.split(':')
        if len(item_data) != 2:
            print(f"Error - invalid parameter '{args}'")
            continue
        item_name = item_data[0]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(item_data[1])
        except ValueError as e:
            print(f"Quantity error for '{item_data[1]}': {e}")
            continue
        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    item_sum = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {item_sum}")
    max_value = None
    min_value = None
    max_key = ""
    min_key = ""
    for item_name in inventory.keys():
        percentage = (inventory[item_name] / item_sum) * 100
        print(f"Item {item_name} represents {round(percentage, 1)}%")
        if max_value is None or inventory[item_name] > max_value:
            max_value = inventory[item_name]
            max_key = item_name
        if min_value is None or inventory[item_name] < min_value:
            min_value = inventory[item_name]
            min_key = item_name
    print(f"Item most abundant: {max_key} with quantity {max_value}")
    print(f"Item least abundant: {min_key} with quantity {min_value}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
