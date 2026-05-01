def secure_archive(file: str, choice: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if choice == "w":
            with open(file, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        elif choice == "r":
            with open(file, "r") as f:
                content = f.read()
            return (True, content)
        return (False, "Invalid mode: use 'r' or 'w'")
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    file = "/not/existing/file"
    result = secure_archive(file, "r", "")
    print(result)
    print()
    print("Using 'secure_archive' to read from  an inaccessibe file:")
    file = "etc/master.passwd"
    result = secure_archive(file, "r", "")
    print(result)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    file = "ancient_fragment.txt"
    result = secure_archive(file, "r", "")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive(file, "w", "This is a test in the archives")
    print(result)
