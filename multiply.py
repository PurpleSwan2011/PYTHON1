def multiply_by_n(number, n):
    return number * n

# Example usage
num = int(input("Enter a number: "))
factor = int(input("Enter the factor to multiply by: "))
result = multiply_by_n(num, factor)

print(f"{num} multiplied by {factor} is {result}")
