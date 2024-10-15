# Função para inverter uma string
def inverter_string(s):
    # Cria uma nova string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona o caractere atual à string invertida
    
    return string_invertida

# Entrada do usuário
entrada_usuario = input("Digite uma string para inverter (ou pressione Enter para usar a string padrão): ")

# String padrão se o usuário não informar nada
if entrada_usuario == "":
    entrada_usuario = "Exemplo de string"

# Inverte a string e exibe o resultado
resultado = inverter_string(entrada_usuario)
print("String invertida:", resultado)
