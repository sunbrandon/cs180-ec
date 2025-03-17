import sys
from coverage_tracker import StatementCoverageTracker

def read_function(filename):
    """Reads the function source code from a file."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python print_cov.py <function_file>")
        sys.exit(1)

    function_file = sys.argv[1]
    input_str = input("Enter the input value: ")
    try:
        input_value = eval(input_str)
    except Exception as e:
        print(f"Error processing input: {e}")
        sys.exit(1)

    function_source = read_function(function_file)

    tracker = StatementCoverageTracker()
    coverage_result = tracker.analyze_function(function_source, input_value)

    print(coverage_result)

if __name__ == "__main__":
    main()
