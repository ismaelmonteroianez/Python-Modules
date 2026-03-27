def input_temperature(temp_str: str) -> int:
    if  int(temp_str) <= 0:
        raise ValueError(f"Caught input_temperature error: {temp_str}°C is too cold for plants (min 0°C)")
    elif int(temp_str) >= 40:
        raise ValueError(f"Caught input_temperature error: {temp_str}°C is too hot for plants (max 40°C)")
    else:
        return int(temp_str)


def test_temperature() -> None:

    ok_temp = "25"
    not_ok_temp = "abc"
    extreme_value1 = "100"
    extreme_value2 = "-50"
    print("=== Garden Temperature Checker===\n")
    try:
        print(f"Input data is '{ok_temp}'")
        result = input_temperature(ok_temp)
        print(f"Temperature is now {result}°C\n")
    except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    try:
        print(f"Input data is '{not_ok_temp}'")
        result = input_temperature(not_ok_temp)
        print(f"Temperature is now {result}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print(f"Input data is '{extreme_value1}'")
        result = input_temperature(extreme_value1)
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print(f"Input data is '{extreme_value2}'")
        result = input_temperature(extreme_value2)
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
