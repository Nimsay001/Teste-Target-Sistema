def verifica_fibonacci(numero):
    # Definindo os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verificando se o número fornecido é igual a um dos primeiros números da sequência
    if numero == a or numero == b:
        return True
    
    # Calculando a sequência de Fibonacci até encontrar um número maior que o fornecido
    while b < numero:
        a, b = b, a + b
        
        # Verificando se o número fornecido pertence à sequência
        if b == numero:
            return True
    
    # Caso o número não seja encontrado na sequência, retorna False
    return False

# Loop infinito
while True:
    # Pedindo ao usuário que forneça um número
    numero_usuario = int(input("Digite um número inteiro para verificar se pertence à sequência de Fibonacci ou 0 para encerrar o programa: "))

    # Verificando se o usuário deseja encerrar o programa
    if numero_usuario == 0:
        break
    
    # Verificando se o número pertence à sequência
    if verifica_fibonacci(numero_usuario):
        print(f"O número {numero_usuario} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero_usuario} não pertence à sequência de Fibonacci.")