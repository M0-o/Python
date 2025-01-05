# Arithmetic Formatter

## Overview

This project provides a function that formats arithmetic expressions (addition and subtraction) in a neat arrangement. It is designed to handle up to five problems at a time, ensuring correct spacing and alignment.

**Note:** My implementation does not use any predefined string formatting functions. Readers are free to develop the functionality in their own way.

## Functionality

- Accepts a list of arithmetic problems in string format.
- Validates the number of problems and checks operators (`+` or `-`).
- Ensures numbers have no more than four digits and include only digits.
- Arranges the problems into aligned columns.
- Supports an optional flag to display the results.

## Steps to implement

1. Parse each problem into operands and operator.
2. Check for errors (e.g., invalid operator, too many digits).
3. Use the length of each operand to determine spacing.
4. Build the formatted string for the top row, operator row, and dashes.
5. If requested, compute and include the result row.

## Usage

1. Import or call `arithmetic_arranger` with a list of strings.
2. Optionally include a boolean to display solutions.
3. The function returns a formatted string or an error message.

## Example

```python
from main import arithmetic_arranger

sample_problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
formatted_output = arithmetic_arranger(sample_problems, True)
print(formatted_output)

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
```
