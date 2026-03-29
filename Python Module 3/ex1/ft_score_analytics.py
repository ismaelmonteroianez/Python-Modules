import sys

def	main() -> None:
	print("=== Player Score Analytics ===")
	if len(sys.argv) == 1:
		print("No scores provided.")
	for i in range(1, len(sys.argv)):
		try:
			float(sys.argv[i])
		except ValueError:
			print(f"Invalid parameter: '{sys.argv[i]}'")
		
if __name__ == "__main__":
	main()
