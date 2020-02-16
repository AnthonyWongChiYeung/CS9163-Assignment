import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input filename")
parser.add_argument("output", help="output filename")
args = parser.parse_args()

img = Image.open(args.input)
width, height = img.size
x1 = y1 = x2 = y2 = 0
if width > height:
    x1 = (width - height) / 2
    x2 = x1 + height
    y2 = height
else:
    y1 = (height - width) /2
    y2 = y1 + width
    x2 = width
img.crop((x1, y1, x2, y2)).save(args.output)
