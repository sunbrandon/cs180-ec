# CS180 Extra Credit: Statement Coverage Tracker

CS180 Extra Credit Assignment

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Features

- Tracks statement coverage for Python functions.
- Supports multiple input types (strings, numbers, arrays).
- Handles loops and recursion with a 2-minute timeout for infinite loops.
- Preserves original code indentation and structure.

## Installation

1. Unzip the `cs180_w25_bsun045.zip`

## Usage

```bash
python3 print_cov.py <function_file> <input_file>
```

Where:
- `<function_file>`: Python file containing the function to test (located in the tests/ directory).
- `<input_file>`: File containing the test input (integer, string, or array)

## Input Format

- The function file should contain one Python function.
- The input file should contain a valid test input.

## Examples

### Example 1: Capitalization Function

Function file (`/tests/capitalize.py`):
```python
def capitalize(sentence: str) -> str:
    """
    Capitalizes the first letter of a sentence or word.

    """
    from string import ascii_lowercase, ascii_uppercase

    if not sentence:
        return ""
    
    # Create a dictionary that maps lowercase letters to uppercase letters
    # Capitalize the first character if it's a lowercase letter
    # Concatenate the capitalized character with the rest of the string
    lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]
```

Input file (`capitalize.txt`):
```
"hello world"
```

Run:
```bash
python print_cov.py tests/capitalize.py tests/capitalize.txt
```

Output:
```
# 1 def capitalize(sentence: str) -> str:
# 2     """
# 3     Capitalizes the first letter of a sentence or word.
# 4 
# 5     """
  6     from string import ascii_lowercase, ascii_uppercase
# 7 
  8     if not sentence:
  9         return ""
# 10 
# 11     # Create a dictionary that maps lowercase letters to uppercase letters
# 12     # Capitalize the first character if it's a lowercase letter
# 13     # Concatenate the capitalized character with the rest of the string
  14     lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
  15     return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]
```

### Example 2: Bubble_Sort_Recursive Function

Function file (`/test/bubble_sort_recursive.py`):
```python
from typing import Any, List

def bubble_sort_recursive(collection: List[Any]) -> List[Any]:
    """It is similar iterative bubble sort but recursive.

    :param collection: mutable ordered sequence of elements
    :return: the same list in ascending order

    """

    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1],
    collection[i]
    swapped = True
    
    return collection if not swapped else bubble_sort_recursive(collection)
```

Input file (`bubble_sort_recursive.txt`):
```
[-23, 0, 6, -4, 34]
```

Run:
```bash
python print_cov.py tests/bubble_sort_recursive.py tests/bubble_sort_recursive.txt
```
Output:
```
# 1 from typing import Any, List
# 2 
# 3 def bubble_sort_recursive(collection: List[Any]) -> List[Any]:
# 4     """It is similar iterative bubble sort but recursive.
# 5 
# 6     :param collection: mutable ordered sequence of elements
# 7     :return: the same list in ascending order
# 8 
# 9     """
# 10 
  11     length = len(collection)
  12     swapped = False
  13     for i in range(length - 1):
# 14         if collection[i] > collection[i + 1]:
# 15             collection[i], collection[i + 1] = collection[i + 1],
# 16     collection[i]
# 17     swapped = True
# 18 
# 19     return collection if not swapped else bubble_sort_recursive(collection)
```
