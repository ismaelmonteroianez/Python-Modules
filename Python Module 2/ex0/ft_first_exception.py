def input_temperature(temp_str: str) -> int:
	return int(temp_str)


def test_temperature() -> None:

    ok_temp = "25"
    not_ok_temp = "abc"
    print("=== Garden Temperature ===")
    try:
        print(f"Input data is '{ok_temp}'")
        result = input_temperature(ok_temp)
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print(f"Input data is '{not_ok_temp}'")
        result = input_temperature(not_ok_temp)
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
