import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    archive: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(archive, "r")
        print("---")
        print()
        content = file.read()
        print(content, end="")
        print("\n")
        print("---")
        file.close()
        print(f"File '{archive}' closed.\n")
        new_content = ""
        for s in content:
            if s == "\n":
                new_content += "#"
            new_content += s
        new_content += "#"
        print("Transform data:")
        print("---")
        print()
        print(new_content, end="")
        print("\n")
        print("---")
        print("Enter new file name (or empty): ", flush=True, end="")
        new_archive: str = sys.stdin.readline()
        new_archive_stripped = new_archive[:len(new_archive) - 1]
        new_archive = new_archive_stripped
        if new_archive == "":
            print("Not saving data.")
        else:
            print(f"Saving data to {new_archive}")
            new_file: typing.IO[str] = open(new_archive, "w")
            new_file.write(new_content)
            print(f"Data saved in file '{new_archive}'.")
            new_file.close()
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file"
              f"'{sys.argv[1]}': {e}", file=sys.stderr)
    except PermissionError as e:
        print(f"[STDERR] Error opening file"
              f"'{sys.argv[1]}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
