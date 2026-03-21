class Plant:
    def __init__(self, name: str, height: int, age: int, growth: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = self.height + self.growth


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30, 0.8)
    plant2 = Plant("Oak", 200, 365, 0.2)
    plant3 = Plant("Cactus", 5, 90, 1.5)
    plant4 = Plant("Sunflower", 80, 45, 0.4)
    plant5 = Plant("Fern", 15, 120, 0.1)
    
    plants = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
