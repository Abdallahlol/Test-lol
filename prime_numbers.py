def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers(n):
    """
    Prints all prime numbers between 2 and n.

    Args:
        n: The upper limit for finding prime numbers.
    """
    print("Prime numbers between 2 and", n, ":")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number (N): "))
            if n < 2:
                raise ValueError("Please enter a number greater than or equal to 2.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print_prime_numbers(n)