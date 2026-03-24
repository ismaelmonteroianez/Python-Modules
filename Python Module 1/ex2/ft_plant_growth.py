class Plant:
    def __init__(self, name: str, height: int,
                 age: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def age_plus(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height = self.height + self.growth


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30, 0.8)
    height = plant1.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.show()
        plant1.age_plus()
        plant1.grow()
    final_height = plant1.height - height
    print(f"Growth this week: {round(final_height)}cm")
