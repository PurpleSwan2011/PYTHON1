# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    try:
        # Validate if the input is a binary number (only contains 0s and 1s)
        if not all(char in '01' for char in binary_str):
            raise ValueError("Input is not a valid binary number.")
        
        # Convert binary string to decimal using int() with base 2
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError as e:
        # Handle invalid input
        return f"Error: {e}"

# Main function
if __name__ == "__main__":
    # Prompt the user for a binary number
    binary_input = input("Enter a binary number: ").strip()
    
    # Convert and display the result
    result = binary_to_decimal(binary_input)
    print(f"Decimal equivalent: {result}")
