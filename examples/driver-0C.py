from tkinter import Image
from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
from goph547lab00.arrays import (
square_ones,
)

# matplotlib - plt work.
def Part_C():
    # loading image
    image = np.asarray(Image.open('examples/rock_canyon.jpg'))
    plt.imshow(image)

if __name__ == '__main__':
    Part_C()