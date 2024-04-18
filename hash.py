import random

def is_prime(n):
    """ Check if a number is a prime number """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_generator(g, p):
    """ Check if g is a generator of the cyclic group Z_p* """
    return set(pow(g, i, p) for i in range(1, p)) == set(range(1, p))

def random_generator(p, exclude_h=None):
    g = random.randint(2, p-1)
    print("Initial random g:", g)
    while not is_generator(g, p) or g == exclude_h:
        g = random.randint(2, p-1)
        print("New random g:", g)
    
    # Print all powers of g
    g_powers = {}
    for i in range(1, p):
        pow_g_i = pow(g, i, p)
        g_powers[pow_g_i] = i
    print("Powers of g for each member:")
    for member in sorted(g_powers):
        print(f"{member} = {g} ^ {g_powers[member]} (mod {p})")

    return g

def hash_function(a, b, g, p, h):
    return (pow(g, a, p) * pow(h, b, p)) % p

def main():
    while True:
        p = int(input("Enter a prime number p: "))
        if is_prime(p):
            break
        print("The number entered is not a prime. Please enter a prime number.")
    
    g = random_generator(p)
    if not is_generator(g, p):
        print("Error: g is not a generator")
        return

    while True:
        h = int(input("Enter a value for h that is not a generator of Z_p*: "))
        if h >= 2 and h < p and not is_generator(h, p):
            break
        print("The value for h is either not within range, is a generator, or is invalid. Please enter another value for h.")

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    hashed_value = hash_function(a, b, g, p, h)
    print("Hashed value:", hashed_value)

if __name__ == "__main__":
    main()
