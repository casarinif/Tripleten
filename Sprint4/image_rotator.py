# imag.py

from PIL import Image
import argparse # importar o módulo argparse

# iniciar o analisador
parser = argparse.ArgumentParser()

# adicionar os argumentos com os nomes correspondentes
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('angle', type=int)

# analisar os argumentos
args = parser.parse_args()

# carregar uma imagem do argumento input_file
im = Image.open(args.input_file)

# exibir tamanho da imagem
print(im.size)

# girar a imagem em um ângulo indicado como um dos argumentos
rotated = im.rotate(args.angle)

# salvar a imagem rodada usando o caminho de saída do argumento output_file
rotated.save(args.output_file)