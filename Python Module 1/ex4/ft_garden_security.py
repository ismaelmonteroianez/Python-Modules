class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def advance_age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height = self._height + self.growth

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")


if __name__ == "__main__":
    plant1 = Plant("Rose", 15, 10, 0.8)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1.show()
    print()
    new_age = 20
    new_height = 30
    plant1.set_age(new_age)
    plant1.set_height(new_height)
    print()
    print("Current state: ", end="")
    plant1.show()
