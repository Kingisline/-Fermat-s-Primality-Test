# Fermat's Primality Test

This repository provides an implementation of Fermat's primality test, a probabilistic method to determine whether a given number is prime.

## Table of Contents
- [Introduction](#introduction)
- [Fermat's Primality Test](#fermats-primality-test)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Prime numbers play a crucial role in various fields such as cryptography, number theory, and computer science. This repository offers a simple and efficient way to check for primality using Fermat's theorem.

## Fermat's Primality Test

Fermat's primality test is based on Fermat's little theorem, which states that if `p` is a prime number and `a` is an integer such that `1 <= a < p`, then:



\[ a^{p-1} \equiv 1 \ (\text{mod} \ p) \]



The algorithm involves picking random values of `a` and checking if the above congruence holds. If it does not hold for any `a`, the number is composite. If it holds for several values of `a`, the number is likely prime.

## Usage

To use the Fermat's primality test implementation, follow these steps:

1. Clone the repository:
      ```sh
      git clone https://github.com/yourusername/fermat-primality-test.git

2. Navigate to the project directory:
   ```sh
   cd fermat-primality-test

3. Run the primality test script with a number:
   ```sh
       python main.py

## Examples
Here are some examples of using the Fermat's primality test:

Checking a Prime Number
      ```sh
         python main.py 17
   
 
## Contributing
   Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.
   
   ## License
   This project is licensed under the MIT License. See the LICENSE file for details.
   
   
   ### Fermat's Primality Test Script (`fermat_primality_test.py`)
   Here’s a simple implementation of Fermat's primality test in Python:
   
   ```python
   import math
   
   
   def fun():
       prime =int(input("Enter the prime number: "))
       
   # base value or it can be changed as any prime number below the target value.
       a = 2
   
       fermat = prime - 1
       fermat = math.pow(a, fermat)
       # print(fermat)
   
       result = fermat % prime
       if(result == 1):
           print("The given number", prime, "is a prime number")
           pass
       else:
           print("The given number", prime, "is not a prime number")
   
   
   
       
   while True:
       fun()




