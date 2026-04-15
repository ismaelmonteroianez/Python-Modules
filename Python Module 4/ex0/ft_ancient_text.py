import typing
import sys
import typing

def main() -> None:
    print("=== Cyber Archives Recovery ===")
    try:
        archive = open("ft_ancient_text.txt", "r")
    except:
        print("file not found")
    print(f"{archive}")