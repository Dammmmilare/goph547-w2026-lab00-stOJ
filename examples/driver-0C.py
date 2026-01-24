from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# matplotlib - plt work.

def Part_C():
    # loading image
    img = np.asarray(Image.open('examples/rock_canyon.jpg'))
    plt.imshow(img)
    plt.savefig('examples/rock_canyon.png')
    plt.show()

    # Converting the image to greyscale
    grey_scale = np.asarray(Image.open('examples/rock_canyon.jpg').convert("L"))
    plt.imshow(grey_scale, cmap=('gray'))
    plt.savefig('examples/rock_canyon_grey_scale version.png')
    plt.show()

    # Displaying a smaller grey scale image 
    small_grey_scale = grey_scale[0:100, 0:100]
    plt.imshow(small_grey_scale, cmap=('gray'))
    plt.savefig('examples/small_rock_canyon_grey_scale version.png')
    plt.show()

if __name__ == '__main__':
    Part_C()