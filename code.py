def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of a and b.
    """
    result = a + b
    return result


if __name__ == "__main__":
    num1 = 10
    num2 = 20
    addition_result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {addition_result}")

