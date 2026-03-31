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
	#main()
	lists = ["1", "2", "3", "hoal"]
	try:
		result = [int(i) for i in lists]
		print(result)
	except ValueError as e:
		srr = e.args[0]
		print(f"value error {srr[40:]}")
