# faz algo útil
def sign(x):
    """Retorna o sinal de número."""
    if x == None:
        return None
    if x < 0:
        return -1
    else:  # Adicione esta condição para números positivos
        return 1


# testa a função de sinal
def test_sign():
    assert sign(-10) == -1  # Correto
    assert sign(10) == 1   # Correto
    # Remova: assert None == 1
 