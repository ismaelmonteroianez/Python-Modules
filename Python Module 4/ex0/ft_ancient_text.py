import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    archive: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{archive}'")
    try:
        file: typing.IO[str] = open(archive, "r")
        print("---")
        print()
        print(file.read())
        print()
        print("---")
        file.close()
        print(f"File '{archive}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{archive}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{archive}': {e}")
    except Exception as e:
        print(f"Error opening file '{archive}': {e}")


if __name__ == "__main__":
    main()
