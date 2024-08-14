def find_smallest_divisor(n: int) -> int:
    """
    Finds the smallest divisor of the given number n greater than 1.
    If no such divisor exists, returns n itself, indicating that n is prime.

    Parameters:
        n (int): The number to find the smallest divisor for.

    Returns:
        int: The smallest divisor of n greater than 1, or n itself if n is prime.
    """
    if n <= 1:
        return n

    d = 2
    while d < n:
        if n % d == 0:
            return d
        d += 1

    return n

n = int(input("Enter a number: "))
print(find_smallest_divisor(n))


