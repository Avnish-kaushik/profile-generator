from config import (
    PROFILE_IMAGE,
    ASCII_OUTPUT
)

from utils import (
    load_image,
    resize_image,
    grayscale,
    image_to_ascii
)


image = load_image(PROFILE_IMAGE)

image = resize_image(image)

image = grayscale(image)

ascii_lines = image_to_ascii(image)

svg = []

svg.append(
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="420" height="520">'
)

svg.append(
    '<rect width="100%" height="100%" fill="#0d1117"/>'
)

y = 18

for line in ascii_lines:

    svg.append(

        f'<text x="10" y="{y}" '
        f'font-family="monospace" '
        f'font-size="8" '
        f'fill="#58a6ff">'
        f'{line}'
        f'</text>'

    )

    y += 8

svg.append("</svg>")

ASCII_OUTPUT.write_text(

    "\n".join(svg),

    encoding="utf-8"

)

print("ASCII SVG generated.") 