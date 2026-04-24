class Plant:
    def __init__(self, name: str, height: float,
                 age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def advance_age(self, days: int = 1) -> None:
        self._age += days

    def grow(self, growth: float = 0.8) -> None:
        self._height = self._height + growth

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

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")


if __name__ == "__main__":
    plant1 = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1.show()
    print()
    new_age = 30
    new_height = 25
    plant1.set_height(new_height)
    plant1.set_age(new_age)
    print()
    new_age = -3
    new_height = -5
    plant1.set_height(new_height)
    plant1.set_age(new_age)
    print()
    print("Current state: ", end="")
    plant1.show()
