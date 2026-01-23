import numpy as np
from goph547lab00.arrays import (
square_ones,
)
# numpy - np work.
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

# Creating an array A with 3 rows and z3 columns
    print ("\nCreating an array A with 3 rows and 3 columns:")
    A = np.array([[5, 7, 2],
                  [1, -2, 3],
                  [4, 4, 4]])
    print(f'A:\n{A}')

# With a single command produce array B with ones in its leading diagonal and zeros elsewhere.
    print ("\nCreating array B with ones in its leading diagonal and zeros elsewhere:")
    B = np.eye(3)
    print(f'B:\n{B}')

# Perform element wise mrultiplication of arrays A and B to produce array C.
    print ("\nPerforming element-wise multiplication of arrays A and B to produce array C:")
    C = A * B
    print(f'C:\n{C}')

# Calculate the dot product of arrays A and B to produce array D.
    print ("\nCalculating the dot product of arrays A and B to produce array D:")
    D = np.dot(A, B)
    print(f'D:\n{D}')

# Calculating the cross product of arrays A and B to produce array E.
    print ("\nCalculating the cross product of arrays A and B to produce array E:")
    E = np.cross(A, B)
    print(f'E:\n{E}')

if __name__ == '__main__':
    Part_B()