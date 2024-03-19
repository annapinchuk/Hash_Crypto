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

## Requirements

- Python 3.x

## Disclaimer

This script is provided for educational purposes and should not be used as a cryptographic primitive without further analysis and enhancement.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.


