def secure_archive(file: str, choice: str = "w", content: str = "") -> tuple[bool, str]:
    try:
        with open(file, choice) as f:
            if choice == "w":
                f.write(content)
                return (True, "'Content successfully written to file'")
            if choice == "r":
                content = f.read()
                return (True, content)
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
    print (result)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    file = "/etc/master.passwd"
    result = secure_archive(file,"r", "")
    print (result)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    file = "ancient_fragment.txt"
    result = secure_archive(file, "r", "")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive(file, "w", "")
