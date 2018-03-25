# Image Resizer

This script is small *Pillow* library wrapper, to simplify image resizing. 
You can use parameters to resize image:
1. **-W, --width**
Image result width. Other side will be scaled, to save image proportions, if height argument not specified
2. **-H, --height**
Image result height. Other side will be scaled, or save image proportions, if width argument not specified
3. **-S, --scale**
Image result scale. Using this argument, it will ignore width and height parameters
4. **-I, --input**  
Input image for resize. Must be jpg or png image format
5. **-O, --output** 
Where save result image. If not specified, script will save result with format: [*name of original file*]_[*width*]x[*height*]

# Quickstart

To launch this script you need python3 installed
Use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Example of script launch on Linux, __Python 3.5__:

```bash
$ python3 image_resize.py -I image.png -W 100
resized image saved as image_100x105.png
$ python3 image_resize.py -I image.png -S .3 -O thumnail.png
resized image saved as thumnail.png
$ python3 image_resize.py -I image.png -W 100 -H 100 -O rectangle.png
resized image saved as rectangle.png
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


# Anti-Duplicator

This script searches directory _default_ in current working directory and find file duplicates in it
Two files are considered duplicate, if they have same name and same size. Content may be different.

You can specify input directory with parameter __-p__ or __--path__
