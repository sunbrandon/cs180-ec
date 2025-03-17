import sys
import ast
import threading
from builtins import enumerate

class StatementCoverageTracker:
    def __init__(self, timeout=120):
        self.timeout = timeout
        self.executed_lines = set()
        self.source_lines = []
        self.line_offset = 0
        self.timed_out = False

    def trace_execution(self, frame, event, arg):
        """Trace executed lines."""
        if event == "line":
            # Adjust by offset so line numbers match the source file
            lineno = frame.f_lineno - self.line_offset
            self.executed_lines.add(lineno)
        return self.trace_execution

    def timeout_handler(self):
        """Handle execution timeout (for infinite loops)."""
        self.timed_out = True
        sys.settrace(None)

    def run_with_coverage(self, func, input_value):
        """Run the function while tracking coverage."""
        self.timed_out = False
        timer = threading.Timer(self.timeout, self.timeout_handler)
        try:
            timer.start()
            sys.settrace(self.trace_execution)
            func(input_value)
        except Exception:
            pass
        finally:
            timer.cancel()
            sys.settrace(None)

    def format_coverage(self):
        """
        Format the coverage output to match the EXACT lines you provided.
        Key points:
        - The 'def' line is always marked '#'.
        - Docstring lines are always marked '#' (multi-line docstrings).
        - Blank lines and comments are always '#'.
        - Other lines are '#' unless actually executed.
        """
        lines_output = []
        in_docstring = False  # Track whether we're inside a triple-quoted docstring

        for i, line in enumerate(self.source_lines, start=1):
            # Default prefix based on actual execution coverage
            prefix = " " if i in self.executed_lines else "#"
            stripped_line = line.strip()

            # Check for triple quotes to toggle docstring mode
            # (This is a simple approach that works for typical multi-line docstrings.)
            if ('"""' in stripped_line) or ("'''" in stripped_line):
                # Toggle docstring state
                in_docstring = not in_docstring
                prefix = "#"  # Force docstring lines to '#'

            # If we're inside a docstring, keep marking lines '#'
            if in_docstring:
                prefix = "#"

            # Force function definition lines to '#'
            if stripped_line.startswith("def "):
                prefix = "#"

            # Force blank lines or comment lines to '#'
            if not stripped_line or stripped_line.startswith("#"):
                prefix = "#"

            lines_output.append(f"{prefix} {i} {line.rstrip()}")

        return "\n".join(lines_output)

    def analyze_function(self, func_source, input_value):
        """Analyze a function and return statement coverage."""
        try:
            tree = ast.parse(func_source)
        except SyntaxError:
            raise SyntaxError("Invalid Python syntax in function file.")

        # Find the first function definition in the file
        func_node = None
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                func_node = node
                break

        if func_node is None:
            raise ValueError("No function definition found in the source.")

        # Set the line offset based on the function definition's starting line
        self.line_offset = func_node.lineno - 1
        self.source_lines = func_source.splitlines()

        namespace = {}
        exec(func_source, namespace)
        func_name = func_node.name
        func = namespace.get(func_name)

        self.run_with_coverage(func, input_value)
        return self.format_coverage()

