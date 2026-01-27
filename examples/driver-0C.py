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

    # with the x-coordinate on the horizontal axis and colour 
    # values on the vertical axis. and with the y-coordinate on the vertical 
    # axis and colour values on the horizontal axis

    # Separate RGB channels
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    # Mean along y-direction (x profiles)
    R_x = np.mean(R, axis=0)
    G_x = np.mean(G, axis=0)
    B_x = np.mean(B, axis=0)
    RGB_x = np.mean(img, axis=(0, 2))

    # Mean along x-direction (y profiles)
    R_y = np.mean(R, axis=1)
    G_y = np.mean(G, axis=1)
    B_y = np.mean(B, axis=1)
    RGB_y = np.mean(img, axis=(1, 2))

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # (i) Mean RGB vs x-coordinate
    ax1.plot(R_x, color='red', label='R')
    ax1.plot(G_x, color='green', label='G')
    ax1.plot(B_x, color='blue', label='B')
    ax1.plot(RGB_x, color='black', linewidth=2, label='Mean RGB')
    ax1.set_xlabel('x-coordinate (pixels)')
    ax1.set_ylabel('Mean colour value')
    ax1.set_title('Mean RGB values vs x-coordinate')
    ax1.legend()

    # (ii) Mean RGB vs y-coordinate
    ax2.plot(R_y, np.arange(len(R_y)), color='red', label='R')
    ax2.plot(G_y, np.arange(len(G_y)), color='green', label='G')
    ax2.plot(B_y, np.arange(len(B_y)), color='blue', label='B')
    ax2.plot(RGB_y, np.arange(len(RGB_y)), color='black', linewidth=2, label='Mean RGB')
    ax2.set_xlabel('Mean colour value')
    ax2.set_ylabel('y-coordinate (pixels)')
    ax2.set_title('Mean RGB values vs y-coordinate')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('examples/rock_canyon_RGB_summary.png', dpi=300)
    plt.show()
if __name__ == '__main__':
    Part_C()