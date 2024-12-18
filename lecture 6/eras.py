def primes(n:int)->list:
    """
    Find all prime numbers up to a given number n.

    This function uses the Sieve of Eratosthenes algorithm to find all prime numbers up to and including n. It returns a list of these prime numbers.

    Parameters:
    n (int): The upper limit (inclusive) to find prime numbers.

    Returns:
    list: A list of prime numbers up to and including n.

    Example:
    >>> primes(10)
    [2, 3, 5, 7]
    """
    primes_mask = [True]*(n+1) # True if prime, False is not prime

    primes = []
    for num in range(2,n):
        if primes_mask[num]:
            primes.append(num)
            for k in range(2*num, n, num):
                primes_mask[k] = False
    return primes
print(primes(30))