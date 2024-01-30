# resizer.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file path')
parser.add_argument('output_file', help='output file path')
parser.add_argument('width', help='largura desejada', type=int)
parser.add_argument('height', help='altura desejada', type=int)
args = parser.parse_args()

im = Image.open(args.input_file)
new_size = (args.width, args.height)
resized = im.resize(new_size)
resized.save(args.output_file)
im.close()