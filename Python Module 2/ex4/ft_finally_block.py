class GardenError(Exception):  
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message= "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant_name: str) -> None:
    raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def check_water(water: int) -> None:
    raise WaterError (f"Not enough water in the tank!")


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    for i in plants:
        try:
            water_plant("Tomato")
            water_plant("Lettuce")
            water_plant("Carrots")
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system\n")


def main():
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)
    print("Testing invalid plants...")
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)


if __name__ == "__main__":
	main()
