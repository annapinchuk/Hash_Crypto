import random

# get random INTEGER from the Cyclic group and check if it is a generator of the group, if not get another random integer
def random_generator(p):
    g = random.randint(2, p-1)
    print("Random g:", g)
    # while g is not a generator of p or  = 31, get another random integer
    while not is_generator(g, p) or g == 31:
        g = random.randint(2, p-1)
    # print all the pows of g to check if it is a generator of p
    g_powers = {}
    for i in range(1, p):
        pow_g_i = pow(g, i, p)
        g_powers[pow_g_i] = i
    print("Powers of g for each member:")
    for member in sorted(g_powers):
        print(f"{member} = {g} ^ {g_powers[member]} (mod {p})")
    return g
 
# check if g is a generator of p
def is_generator(g, p):
    return set(pow(g, i, p) for i in range(1, p)) == set(range(1, p))


def hash_function(a, b, g, p, h):
    return (pow(g, a, p) * pow(h, b, p)) % p

def main():
    p = 101
    g = random_generator(p)
    #check if g is a generator
    if not is_generator(g, p):
        print("Error: g is not a generator")
        return
    h = 31

    # ask for a and b
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    hashed_value = hash_function(a, b, g, p, h)
    print("Hashed value:", hashed_value)

if __name__ == "__main__":
    main()
