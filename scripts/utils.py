from PIL import Image
from pathlib import Path


def load_image(path):
    """
    Opens an image safely.
    """

    if not Path(path).exists():
        raise FileNotFoundError(f"Image not found: {path}")

    return Image.open(path)


def resize_image(image, width=90):
    """
    Resize image while maintaining aspect ratio.
    """

    aspect_ratio = image.height / image.width

    height = int(width * aspect_ratio * 0.55)

    return image.resize((width, height))


def grayscale(image):
    """
    Convert image to grayscale.
    """

    return image.convert("L")


ASCII_CHARS = (
    "@",
    "#",
    "S",
    "%",
    "?",
    "*",
    "+",
    ";",
    ":",
    ",",
    ".",
    " "
)


def pixel_to_char(pixel):
    """
    Convert brightness to ASCII character.
    """

    return ASCII_CHARS[pixel * (len(ASCII_CHARS)-1) // 255]


def image_to_ascii(image):

    pixels = image.getdata()

    ascii_string = "".join(pixel_to_char(pixel) for pixel in pixels)

    width = image.width

    lines = [
        ascii_string[index:index + width]
        for index in range(0, len(ascii_string), width)
    ]

    return lines 