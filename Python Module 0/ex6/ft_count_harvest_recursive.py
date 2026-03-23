def recursive(days_left):
    if (days_left == 0):
        return
    recursive(days_left - 1)
    print("Day", days_left)


def ft_count_harvest_recursive():
    days_left = int(input("Days until harvest: "))
    recursive(days_left)
    print("Harvest time!")
