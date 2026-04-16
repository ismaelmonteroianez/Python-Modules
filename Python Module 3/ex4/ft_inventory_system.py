import sys


def main() -> None:
    inventory = {}
    for args in sys.argv[1:]:
        accumulattor = ""
        accumulattor2 = ""
        item_name = ""
        colon = False
        for x in args:
            if x == ':':
                colon = True
                continue
            elif colon is False:
                accumulattor = accumulattor + x
            if colon is True:
                accumulattor2 = accumulattor2 + x
        try:
            item_name = accumulattor
            if colon is False:
                print(f"Error - invalid parameter '{item_name}'")
                continue
            quantity = int(accumulattor2)
            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
            else:
                inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")
    item_list = list(dict.keys(inventory))
    print(f"Item list: {item_list}")
    item_sum = sum(dict.values(inventory))
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
