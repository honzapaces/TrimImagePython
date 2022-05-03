# Implement an algorithm that will 'trim' image to the minimum size removing unnecessary transparent borders. For ease
# of use we recommend the Image from Pillow library, transparency layer (if-present) is represented by alpha channel.
# Image documentation https://pillow.readthedocs.io/en/stable/reference/Image.html
# Implement get_triming_rectangle function

from PIL import Image


def trim_image(path):
    i = Image.open(path)
    cropped_image = i.crop(get_trimming_rectangle(i))
    save_image(cropped_image, path)


def save_image(cropped_image, path):
    filename_split = path.split('.')
    cropped_image.save(filename_split[0] + '_trimmed.' + filename_split[1])


def get_trimming_rectangle(image_to_trim):
    """
    TODO - Implement this
    """
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageList = ['image.png', 'image1.png']
    for image in imageList:
        trim_image(image)