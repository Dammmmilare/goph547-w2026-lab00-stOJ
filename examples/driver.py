import numpy as np
from goph547lab00.arrays import (
square_ones,
)
def main():
# test creating square array of ones
    A_np = np.ones((3,3))
    A = square_ones(3)
    print(f'A_np:\n{A_np}')
    print(f'A:\n{A}')
if __name__ == '__main__':
    main()

def Part_B():
# Creating an array of ones with 3 rows and 5 columns
    B_np = np.ones((3, 5))
    B = square_ones(3)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')
# Creating an array of NaN with 3 rows and 5 columns
    B_np = np.NaN((3, 5))
    B = square_NaN(3)
    print(f'B_np:\n{B_np}')
    print(f'B:\n{B}')
if __name__ == '__main__':
    PartB()