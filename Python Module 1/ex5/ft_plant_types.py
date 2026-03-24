class Plant:
    def __init__(self, name: str, height: int,
                 age: int, growth: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> int:
        return self._height

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")


class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, growth: float, color: str) -> None:
        self.color = color
        super().__init__(name, height, age, growth)

    def show(self) -> None:
        print("=== Flower")
        super().show()
        print(f" Color {self.color}")

    def bloom(self) -> None:


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print("=== Tree")
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 growth: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print("=== Vegetable")
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    plant1 = Flower("Rose", 15, 10, 0.8, "red")
    plant2 = Tree("Oak", 200, 365, 0.2, 5.0)
    plant3 = Vegetable("Tomato", 5, 10, 0.1, "April", 0)
    print("=== Garden Plant Types ===")
    plant1.show()
    print("[asking the rose to bloom]")

