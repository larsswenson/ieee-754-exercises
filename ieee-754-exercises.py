import struct
import numpy as np
import matplotlib.pyplot as plt

# Convert decimal to IEEE 754
def float_to_ieee754(num):
    packed = struct.pack('>f', num)
    unpacked = struct.unpack('>I', packed)[0]
    return f'{unpacked:032b}'

# Arithmetic operations
def ieee754_operations():
    a, b = 0.1, 0.2
    c = a + b
    ieee_c = float_to_ieee754(c)
    
    d = 1.0 / 3.0
    ieee_d = float_to_ieee754(d)
    
    print(f'0.1 + 0.2 = {c} -> IEEE 754: {ieee_c}')
    print(f'1.0 / 3.0 = {d} -> IEEE 754: {ieee_d}')
    
    # Discrepancies
    print("\nExplanation of discrepancies:")
    print("Due to binary representation of decimals, some numbers can't be represented exactly in IEEE 754 format, resulting in precision loss.")

# Special values 
def special_values():
    pos_inf = float('inf')
    neg_inf = float('-inf')
    nan = float('nan')
    
    print(f'Positive infinity: {pos_inf}, IEEE 754: {float_to_ieee754(pos_inf)}')
    print(f'Negative infinity: {neg_inf}, IEEE 754: {float_to_ieee754(neg_inf)}')
    print(f'NaN: {nan}, IEEE 754: {float_to_ieee754(nan)}, NaN != NaN: {nan != nan}')

# Rounding - Python's default is round to nearest
def rounding_modes():
    print("\nRounding modes:")
    print(f'round(2.5) -> {round(2.5)}')
    print(f'round(3.5) -> {round(3.5)}')

# Underflow & overflow
def underflow_overflow():
    small_num = 1e-40
    large_num = 1e+40
    underflow_result = small_num / 2
    overflow_result = large_num * 2
    
    print("\nUnderflow and Overflow:")
    print(f'Underflow result: {underflow_result}')
    print(f'Overflow result: {overflow_result}')

# Precision loss
def precision_loss():
    x = np.linspace(1e-40, 1e-30, 100)
    y = x / 2
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Precision Loss')
    plt.xlabel('Input Value')
    plt.ylabel('Result (Value / 2)')
    plt.title('Precision Loss for Very Small Numbers')
    plt.legend()
    plt.show()

# Comparative study
def comparative_study():
    print("\nComparative Study:")
    print("Different languages may have alternate default rounding modes and exception handling for instances like overflow and underflow.")
    print("For example, Python's default is round to nearest, while some other languages may use round toward zero.")

# Test cases
def test_cases():
    print("\nTest Cases:")
    
    # Normal cases
    test_values = [0.1, 1.0, 45.25]
    expected_ieee754 = [
        "00111101110011001100110011001101",
        "00111111100000000000000000000000",
        "01000010001101010000000000000000"
    ]
    for val, expected in zip(test_values, expected_ieee754):
        ieee_val = float_to_ieee754(val)
        assert ieee_val == expected, f"Test failed for {val}: expected {expected}, got {ieee_val}"
        print(f"Test passed for {val}: {ieee_val}")

    # Edge cases
    special_values_list = [float('inf'), float('-inf'), float('nan')]
    expected_special_values = [
        "01111111100000000000000000000000",
        "11111111100000000000000000000000",
        "01111111110000000000000000000000"
    ]
    for val, expected in zip(special_values_list, expected_special_values):
        ieee_val = float_to_ieee754(val)
        assert ieee_val == expected, f"Test failed for {val}: expected {expected}, got {ieee_val}"
        print(f"Test passed for {val}: {ieee_val}")

def main():
    print("Decimal to IEEE 754 conversion:")
    print(float_to_ieee754(45.25))

    ieee754_operations()
    special_values()
    rounding_modes()
    underflow_overflow()
    precision_loss()
    comparative_study()
    test_cases()

if __name__ == "__main__":
    main()
