# # module.py
#
# import re
#
# def check_email(string: str):
#     '''
#     use expressões regulares para verificar a formatação do endereço de e-mail
#     o padrão é "algo@algo.algo"
#     '''
#     if re.match('[.\w]+@\w+[.]\w+', string):
#         print('correto')
#     else:
#         print('verifique endereço de e-mail')
#
# def check_age(age: int):
#     if age >= 50:
#         print('acesso concedido')
#     else:
#         print("você é muito jovem")



# module_1.py

def useful_function():
    print('funcionando codigo module')

if __name__ == '__main__':
    print("testando a função...")
    useful_function()