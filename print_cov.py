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

def read_input(filename):
    """Reads the test input from a file and evaluates it."""
    try:
        with open(filename, "r") as file:
            return eval(file.read().strip())
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python print_cov.py <function_file> <input_file>")
        sys.exit(1)

    function_file = sys.argv[1]
    input_file = sys.argv[2]

    function_source = read_function(function_file)
    test_input = read_input(input_file)

    tracker = StatementCoverageTracker()
    coverage_result = tracker.analyze_function(function_source, test_input)
    print(coverage_result)

if __name__ == "__main__":
    main()
