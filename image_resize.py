from PIL import Image
from pathlib import Path
import argparse
import sys


def calculate_size_by_width(target_width, width, height):
    target_height = height * target_width / width
    return target_width, target_height


def calculate_size_by_height(target_height, width, height):
    target_width = width * target_height / height
    return target_width, target_height


def calculate_size_by_scale(scale, width, height):
    return width*scale, height*scale


def get_args():
    parser = argparse.ArgumentParser()
    width_help = """Image result width. Other side will be scaled, to save
image proportions, if height argument not specified"""
    height_help = """Image result height. Other side will be scaled, ot save
image proportions, if width argument not specified"""
    scale_help = """Image result scale. Using this argument, it will
ignore width and height parameters"""
    input_help = "Input image for resize. Must be jpg or png image format"
    output_help = """Where save result image. If not specified, it will
            save it in format: [name of original file]_[width]x[height]"""
    parser.add_argument(
        "-W",
        "--width",
        dest="width",
        help=width_help
    )
    parser.add_argument(
        "-H",
        "--height",
        dest="height",
        help=height_help
    )
    parser.add_argument(
        "-S",
        "--scale",
        dest="scale",
        help=scale_help
    )
    parser.add_argument(
        "-I"
        "--input",
        dest="input_file",
        help=input_help
    )
    parser.add_argument(
        "-O",
        "--output",
        dest="output",
        help=output_help
    )
    return parser.parse_args()


def resize(input_path, params, output_path):
    image = Image.open(input_path)
    if params.scale:
        size = calculate_size_by_scale(float(params.scale), *image.size)
    elif params.width and not params.height:
        size = calculate_size_by_width(float(params.width), *image.size)
    elif params.height and not params.width:
        size = calculate_size_by_height(float(params.height), *image.size)
    elif params.width and params.height:
        size = float(params.width), float(params.height)
    else:
        return None
    size = tuple([round(x) for x in size])

    image_path = Path(params.input_file)
    suffix = image_path.suffix[1:]

    if not output_path:
        output_path = "{}_{}x{}.{}".format(
            image_path.stem,
            size[0],
            size[1],
            suffix
        )
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(output_path, suffix)
    return output_path


if __name__ == "__main__":
    args = get_args()
    if not args.input_file:
        sys.exit("input image required")
    if not args.scale and not args.width and not args.height:
        sys.exit("please specify any resize parameters")
    if args.scale:
        if args.width or args.height:
            sys.exit("if scale specified, width and height forbidden")
    output_path = resize(args.input_file, args, args.output)
    if output_path:
        print("resized image saved as {}".format(output_path))
    else:
        print("error: image not resized")
