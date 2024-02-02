# f = open('my_file.txt')
# print(f.read())
# f.close()
#
# print() # imprimindo uma linha vazia para separar as linhas
#
# f = open('my_file.txt')
# print(f.readlines())
# f.close()

# with open('my_file.txt') as f:
#     for line in f.readlines():
#         print(line.rstrip())


from datetime import datetime

# obter a hora atual
# now = datetime.now()
#
# with open('my_journal.txt', 'a') as f:
#     f.write('\n')     # começar uma nova linha
#     f.write(str(now)) # marca temporal
#     f.write('\n\n')   # inserir uma linha em branco
#     f.write(' ')      # espaço vazio
#     f.write(input())  # digitar uma entrada de diário no teclado
#     f.write('\n\n')  # terminar com uma linha em branco

titles = ['Planeta do futuro\n', 'Soluções para um mundo sustentável\n', "A cidade mais poluída do mundo\n"]

with open('output.txt', 'w') as f:
    f.writelines(titles)