import math

def is_prime(num_primo):
    """
    Verifica se um número é primo.

    Args:
        num_primo: O número inteiro a ser verificado.

    Returns:
        True se num_primo for primo, False caso contrário.
    """

    if num_primo <= 1:
        return False
    for i in range(2, int(math.sqrt(num_primo)) + 1):
        if num_primo % i == 0:
            return False
    return True

def main():
    """
    Imprime os primeiros 100 números primos.
    """

    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()

if __name__ == '__main__':
    main()
