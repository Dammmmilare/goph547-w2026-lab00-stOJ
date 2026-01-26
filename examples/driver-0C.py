from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# matplotlib - plt work.

def Part_C():
    # loading image
    img = np.asarray(Image.open('examples/rock_canyon.jpg'))
    plt.imshow(img)
    plt.savefig('examples/rock_canyon.png')
    plt.axis('off')
    plt.show()
    print("Image shape:", img.shape)

    # Converting the image to greyscale
    grey_scale = np.asarray(Image.open('examples/rock_canyon.jpg').convert("L"))
    plt.imshow(grey_scale, cmap=('gray'))
    plt.savefig('examples/rock_canyon_grey_scale version.png')
    plt.axis('off')
    plt.show()
    print("Grey scale image shape:", grey_scale.shape)

    # Displaying a smaller grey scale image 
    x, y = grey_scale.shape
    small_grey_scale = grey_scale[int(0.3*y):int(0.55*y), int(0.35*x):int(0.55*x)]
    plt.imshow(small_grey_scale, cmap=('gray'))
    plt.savefig('examples/small_rock_canyon_grey_scale version.png')
    plt.axis('off')
    plt.show()
    print("Small grey scale image shape:", small_grey_scale.shape)

    # Making subplots with two plots.
    # with the x-coordinate on the horizontal axis and colour values on the vertical axis.
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(grey_scale[200, :], color='black')
    ax1.set_title('Grey Scale Image Row 200')
    ax2.plot(img[200, :, 0], color='red', label='Red Channel')
    ax2.plot(img[200, :, 1], color='green', label='Green Channel')
    ax2.plot(img[200, :, 2], color='blue', label='Blue Channel')
    ax2.set_title('RGB Image Row 200') 
    ax2.legend()
    plt.tight_layout()
    plt.savefig('examples/rock_canyon_RGB_Summary.png')
    plt.show()

    #with the y-coordinate on the vertical axis and colour values on the horizontal axis.
    fig, (ay1, ay2) = plt.subplots(2)
    ay1.plot(grey_scale[:, 200], color='black')
    ay1.set_title('Grey Scale Image Column 200')
    ay2.plot(img[:, 200, 0], color='red', label='Red Channel')
    ay2.plot(img[:, 200, 1], color='green', label='Green Channel')
    ay2.plot(img[:, 200, 2], color='blue', label='Blue Channel')
    ay2.set_title('RGB Image Column 200') 
    ay2.legend()
    plt.tight_layout()
    plt.savefig('examples/rock_canyon_RGB_Summary2.png')
    plt.show()

if __name__ == '__main__':
    Part_C()