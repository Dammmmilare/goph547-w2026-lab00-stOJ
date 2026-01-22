import numpy as np
from goph547lab00.arrays import (
square_ones,
)

def Part_B():
# Creating an array of ones with 3 rows and 5 columns.
    print ("\nCreating an array of ones with 3 rows and 5 columns:")
    B_np = np.ones((3, 5))
    B = square_ones(3)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')

# Creating an array of NaN with 3 rows and 5 columns.
    print ("\nCreating an array of NaN with 3 rows and 5 columns:")
    B_np = np.full((6, 3), np.nan)
    B = np.full((6, 3), np.nan)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')

# Creating a column vector of odd numbers between 44 and 75.
    print ("\nCreating an array of odd numbers from 44 to 75 in a single column:")
    odd_numbers = np.arange(45, 76, 2).reshape(-1, 1)
    print(odd_numbers)

# Finding the sum of column vector of odd numbers between 44 and 75.
    print ("\nFinding the sum of odd numbers from 44 to 75:")
    print(f"Sum of odd numbers: {np.sum(odd_numbers)}")

if __name__ == '__main__':
    Part_B()