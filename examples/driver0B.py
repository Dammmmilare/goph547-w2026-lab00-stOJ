import numpy as np
from goph547lab00.arrays import (
square_ones,
)

def Part_B():
# Creating an array of ones with 3 rows and 5 columns
    print ("\nCreating an array of ones with 3 rows and 5 columns:")
    B_np = np.ones((3, 5))
    B = square_ones(3)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')

# Creating an array of NaN with 3 rows and 5 columns
    print ("\nCreating an array of NaN with 3 rows and 5 columns:")
    B_np = np.full((3, 5), np.nan)
    B = np.full((3, 5), np.nan)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')
    
if __name__ == '__main__':
    Part_B()