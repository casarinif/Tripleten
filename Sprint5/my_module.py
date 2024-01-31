# my_module.py

import re

def email_check(string: str):
      '''
      Use expressões regulares para verificar a formatação do endereço de e-mail:
      o padrão é "algo@algo.algo"
      '''
      if re.match('[.\w]+@\w+[.]\w+', string):
            print('correto')
      else:
            print('endereço de e-mail errado')

def age_check(age: int):
      '''
      Verifique se a idade está dentro do limite
      '''
      if age >= 50:
            print('acesso concedido')
      else:
            print("você é muito jovem")