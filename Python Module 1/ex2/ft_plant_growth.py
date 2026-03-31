class Plant:
    def __init__(self, name: str, height: float,
                 age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def advance_age(self, days: int = 1) -> None:
        self.age += days

    def grow(self, growth: float = 0.8) -> None:
        self.height = self.height + growth


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30)
    height = plant1.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.show()
        plant1.advance_age()
        plant1.grow()
    final_height = plant1.height - height
    print(f"Growth this week: {round(final_height)}cm")
