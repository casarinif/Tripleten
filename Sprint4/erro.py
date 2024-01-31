# image_rotator.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='caminho do arquivo de entrada')
parser.add_argument('output_file', help='caminho do arquivo de saída')
parser.add_argument('angle', help='rotação desejada', type=int)
parser.add_argument('-i', '--info', help='exibir tamanho da imagem', action='store_true')
args = parser.parse_args()

angle = args.angle

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    print('Arquivo de entrada não encontrado, forneça o nome do arquivo correto:')
    im = Image.open(input())

except Exception:
    print('Arquivo errado, tente outro:')
    im = Image.open(input())

else:
    print("Funcionando sem problemas")

finally:
    rotated = im.rotate(angle)
    im.close()  # fechando o arquivo da imagem, removendo-o da memória
    rotated.save(args.output_file)

if args.info:
    print('Dimensões da imagem de entrada:', im.size)
