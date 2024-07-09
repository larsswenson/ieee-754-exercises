# IEEE 754 Floating-Point Exercises

This Python program demonstrates various aspects of the IEEE 754 floating-point standard, including conversion, arithmetic operations, handling special values, rounding modes, underflow and overflow, and visualizing precision loss.

## Features

- **Convert Decimal to IEEE 754 Format**: Convert a decimal number to IEEE 754 32-bit single-precision floating-point binary representation.
- **Arithmetic Operations**: Perform arithmetic operations and display results in IEEE 754 format.
- **Special Values Handling**: Generate and verify positive infinity, negative infinity, and NaN.
- **Rounding Modes**: Experiment with different rounding modes and provide examples.
- **Underflow and Overflow**: Demonstrate underflow and overflow with specific examples.
- **Visualizing Precision Loss**: Create a plot to visualize the loss of precision for very small or very large numbers.
- **Comparative Study**: Discuss how different programming languages handle IEEE 754 arithmetic.
- **Test Cases**: Include test cases to verify the correctness of conversions and special values handling.

## Installation

1. Ensure you have Python installed. You can check this by running:
    ```sh
    python3 --version
    ```

2. Install the required packages using `pip`:
    ```sh
    pip3 install numpy matplotlib
    ```

## Usage

1. Clone the repository or download the script file.
2. Open the script file in your preferred editor.
3. Run the script:
    ```sh
    python3 script_name.py
    ```
    Replace `script_name.py` with the actual name of the Python script file.

## Example Output

The program will display IEEE 754 representation of given decimal numbers, perform arithmetic operations, handle special values, demonstrate rounding modes, and visualize precision loss. It will also run test cases to ensure correctness.

## Test Cases

The script includes assertions to verify the correctness of IEEE 754 conversion and handling of special values. If all tests pass, you will see "Test passed" messages. If any test fails, an `AssertionError` will be raised with a message indicating the discrepancy.

### Normal Cases

- 0.1: `00111101110011001100110011001101`
- 1.0: `00111111100000000000000000000000`
- 45.25: `01000010001101010000000000000000`

### Edge Cases

- Positive Infinity: `01111111100000000000000000000000`
- Negative Infinity: `11111111100000000000000000000000`
- NaN: `01111111110000000000000000000000`

## Explanation of Discrepancies

Due to binary representation of decimals, some numbers can't be represented exactly in IEEE 754 format, resulting in precision loss.

## Comparative Study

Different languages may have alternate default rounding modes and exception handling for instances like overflow and underflow. For example, Python's default is round to nearest, while some other languages may use round toward zero.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

