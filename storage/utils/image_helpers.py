import os
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter


__all__ = [
    'add_watermark',
    'get_image_size'
]


def _draw_text_with_halo(img, position, text, font, text_col, halo_col):
    halo = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font=font, fill=halo_col)

    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text, font=font, fill=text_col)
    return Image.composite(img, blurred_halo, ImageChops.invert(blurred_halo))


def set_watermark(font_path,  image_path, msg, img_fmt):
    """
    Add watermark to image

    :param font_path: path to font file
    :param image_path: path to image file
    :param msg: watermark message
    :param img_fmt: watermark image format, e.g. 'JPEG'
    """

    msg_split = textwrap.wrap(msg, width=50)

    original = Image.open(image_path).convert('RGBA')
    font_size = 1
    font = ImageFont.truetype(font_path, font_size)
    while font.getsize(msg_split[0])[0] < original.size[0]:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)

    font_size -= 5
    font = ImageFont.truetype(font_path, font_size)

    W, H = original.size  # size of original image
    txt = Image.new('RGBA', original.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    padding = 10
    text_height = sum([draw.textsize(s, font=font)[1] for s in msg_split]) + padding * len(msg_split)
    current_h = H - text_height * 1.3

    for line in msg_split:
        w, h = draw.textsize(line, font=font)
        halo_col = (0, 0, 0)
        text_col = (255, 255, 255, 60)
        img = _draw_text_with_halo(
            img=original,
            position=((W - w) / 2, current_h),
            text=line,
            font=font,
            text_col=text_col,
            halo_col=halo_col
        )

        original = img
        current_h += h + padding

    original.save(image_path, img_fmt)


def get_image_size(img_path) -> tuple:
    """
    :param img_path: str
    :return: (width, height)
    """
    image = Image.open(img_path)
    return image.size