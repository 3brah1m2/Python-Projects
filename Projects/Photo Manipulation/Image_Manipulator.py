from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    with Image.open(image) as img2:
        img_rgb = img2.convert('RGB')
        enhancer = ImageEnhance.Brightness(img_rgb)
        img_bright = enhancer.enhance(factor)
        img_bright.show()
def adjust_contrast(image, factor):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    with Image.open(image) as img2:
        img_rgb = img2.convert('RGB')
        enhancer = ImageEnhance.Contrast(img_rgb)
        img_bright = enhancer.enhance(factor)
        img_bright.show()

def blur(image, factor):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    with Image.open(image) as img2:
        img_rgb = img2.convert('RGB')
        blurred = img_rgb.filter(ImageFilter.GaussianBlur(radius=factor))
        blurred.show()

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    with Image.open(image) as img2:
        img_rgb = img2.convert('RGB')
        outlined = img_rgb.filter(ImageFilter.FIND_EDGES)
        outlined.show()


def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    # Open two images
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    image2 = image2.resize(image1.size)
    image1 = image1.convert('RGB')
    image2 = image2.convert('RGB')

    image2 = image2.resize(image1.size)

    combined_image = ImageChops.add(image1, image2, scale=2)

    combined_image.show()

combine_images('C:/Users/Ebrahim R/Documents/Python-Projects/Projects/Photo Manipulation/lake.png',
               'C:/Users/Ebrahim R/Documents/Python-Projects/Projects/Photo Manipulation/city.png')