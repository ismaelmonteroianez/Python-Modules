def input_temperature(temp_str: str) -> int:
	return int(temp_str)


def test_temperature() -> None:
      print("=== Garden Temperature ===")
      input_temperature("25")
      input_temperature("abc")

if __name__ == "__main__":
    test_temperature()