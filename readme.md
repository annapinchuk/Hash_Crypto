# Hash Function Implementation

This Python script implements a hash function within a finite cyclic group. The hash function is constructed using discrete logarithms in the context of a prime field.

## Features

- **Generator Selection**: Chooses a random integer and verifies if it's a generator of the cyclic group modulo \( p \).
- **Hash Function**: Utilizes the properties of the cyclic group to compute a hash value based on user inputs.

## How It Works

1. The `random_generator` function selects a random integer and checks if it's a generator of the cyclic group modulo \( p \). If not, it selects another integer.
2. The `is_generator` function verifies if a given integer is a generator by checking if its powers modulo \( p \) produce all elements of the group.
3. The `hash_function` computes the hash value using the generator, another group member, and user-provided inputs \( a \) and \( b \).

## Usage

Run the script using a Python interpreter. You will be prompted to enter values for \( a \) and \( b \), which are used in the hash function calculation.

```bash
python hash_function_script.py
```
Input the values as prompted to obtain the hash value.

## Run Example
random g, h = 31, G = Z∗101 when p=101 
```bash
Enter a prime number p: 101
Initial random g: 38
Powers of g for each member:
1 = 38 ^ 100 (mod 101)
2 = 38 ^ 33 (mod 101)
3 = 38 ^ 77 (mod 101)
4 = 38 ^ 66 (mod 101)
5 = 38 ^ 92 (mod 101)
6 = 38 ^ 10 (mod 101)
7 = 38 ^ 97 (mod 101)
8 = 38 ^ 99 (mod 101)
9 = 38 ^ 54 (mod 101)
10 = 38 ^ 25 (mod 101)
11 = 38 ^ 29 (mod 101)
12 = 38 ^ 43 (mod 101)
13 = 38 ^ 78 (mod 101)
14 = 38 ^ 30 (mod 101)
15 = 38 ^ 69 (mod 101)
16 = 38 ^ 32 (mod 101)
17 = 38 ^ 90 (mod 101)
18 = 38 ^ 87 (mod 101)
19 = 38 ^ 68 (mod 101)
20 = 38 ^ 58 (mod 101)
21 = 38 ^ 74 (mod 101)
22 = 38 ^ 62 (mod 101)
23 = 38 ^ 38 (mod 101)
24 = 38 ^ 76 (mod 101)
25 = 38 ^ 84 (mod 101)
26 = 38 ^ 11 (mod 101)
27 = 38 ^ 31 (mod 101)
28 = 38 ^ 63 (mod 101)
29 = 38 ^ 3 (mod 101)
30 = 38 ^ 2 (mod 101)
31 = 38 ^ 72 (mod 101)
32 = 38 ^ 65 (mod 101)
33 = 38 ^ 6 (mod 101)
34 = 38 ^ 23 (mod 101)
35 = 38 ^ 89 (mod 101)
36 = 38 ^ 20 (mod 101)
37 = 38 ^ 48 (mod 101)
38 = 38 ^ 1 (mod 101)
39 = 38 ^ 55 (mod 101)
40 = 38 ^ 91 (mod 101)
41 = 38 ^ 85 (mod 101)
42 = 38 ^ 7 (mod 101)
43 = 38 ^ 86 (mod 101)
44 = 38 ^ 95 (mod 101)
45 = 38 ^ 46 (mod 101)
46 = 38 ^ 71 (mod 101)
47 = 38 ^ 14 (mod 101)
48 = 38 ^ 9 (mod 101)
49 = 38 ^ 94 (mod 101)
50 = 38 ^ 17 (mod 101)
51 = 38 ^ 67 (mod 101)
52 = 38 ^ 44 (mod 101)
53 = 38 ^ 59 (mod 101)
54 = 38 ^ 64 (mod 101)
55 = 38 ^ 21 (mod 101)
56 = 38 ^ 96 (mod 101)
57 = 38 ^ 45 (mod 101)
58 = 38 ^ 36 (mod 101)
59 = 38 ^ 57 (mod 101)
60 = 38 ^ 35 (mod 101)
61 = 38 ^ 41 (mod 101)
62 = 38 ^ 5 (mod 101)
63 = 38 ^ 51 (mod 101)
64 = 38 ^ 98 (mod 101)
65 = 38 ^ 70 (mod 101)
66 = 38 ^ 39 (mod 101)
67 = 38 ^ 73 (mod 101)
68 = 38 ^ 56 (mod 101)
69 = 38 ^ 15 (mod 101)
70 = 38 ^ 22 (mod 101)
71 = 38 ^ 52 (mod 101)
72 = 38 ^ 53 (mod 101)
73 = 38 ^ 13 (mod 101)
74 = 38 ^ 81 (mod 101)
75 = 38 ^ 61 (mod 101)
76 = 38 ^ 34 (mod 101)
77 = 38 ^ 26 (mod 101)
78 = 38 ^ 88 (mod 101)
79 = 38 ^ 12 (mod 101)
80 = 38 ^ 24 (mod 101)
81 = 38 ^ 8 (mod 101)
82 = 38 ^ 18 (mod 101)
83 = 38 ^ 37 (mod 101)
84 = 38 ^ 40 (mod 101)
85 = 38 ^ 82 (mod 101)
86 = 38 ^ 19 (mod 101)
87 = 38 ^ 80 (mod 101)
88 = 38 ^ 28 (mod 101)
89 = 38 ^ 93 (mod 101)
90 = 38 ^ 79 (mod 101)
91 = 38 ^ 75 (mod 101)
92 = 38 ^ 4 (mod 101)
93 = 38 ^ 49 (mod 101)
94 = 38 ^ 47 (mod 101)
95 = 38 ^ 60 (mod 101)
96 = 38 ^ 42 (mod 101)
97 = 38 ^ 16 (mod 101)
98 = 38 ^ 27 (mod 101)
99 = 38 ^ 83 (mod 101)
100 = 38 ^ 50 (mod 101)
Enter a value for h that is not a generator of Z_p*: 31
Enter a: 5462562
Enter b: 1345145
Hashed value: 30
```
## Requirements

- Python 3.x

## Disclaimer

This script is provided for educational purposes and should not be used as a cryptographic primitive without further analysis and enhancement.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.


