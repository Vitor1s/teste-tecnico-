# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(n):
    # Sequência inicial
    a, b = 0, 1

    # Enquanto o valor b não for maior que n
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    
    return False

# Entrada do usuário (ou você pode definir um valor diretamente)
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando se o número informado pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")