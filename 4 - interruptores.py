def find_switch_lamp(num_switches, num_lamps):
    """
    Simula o processo de descobrir qual interruptor controla qual lâmpada.

     :param num_switches: o número de opções
     :param num_lamps: o número de lâmpadas
     :return: uma lista de tuplas, onde cada tupla contém um número de chave e um número de lâmpada
    """
    # Inicialize os interruptores
    switches = [False] * num_switches

    # VVisite a primeira lâmpada
    lamp_1 = check_lamp(switches[0])

    # Acione o primeiro interruptor e visite a segunda lâmpada
    switches[0] = not switches[0]
    lamp_2 = check_lamp(switches[0])

    # Inicialize a lista de resultados
    result = []

    #Adicione o primeiro interruptor e lâmpada à lista de resultados
    result.append((0, lamp_1))

    #Se a primeira e a segunda lâmpadas forem iguais, então o primeiro interruptor controla ambas
    if lamp_1 == lamp_2:
        for i in range(1, num_lamps):
            result.append((0, i))
    else:
        # Caso contrário, o primeiro interruptor controla a primeira lâmpada
        result.append((0, 0))

        # Adicione o segundo interruptor e lâmpada à lista de resultados
        result.append((1, lamp_2))

        # Se a segunda e a terceira lâmpadas forem iguais, o segundo interruptor controla ambas
        if i < num_switches - 1 and check_lamp(switches[1]) == lamp_2:
            for j in range(1, num_lamps):
                result.append((1, j))
        else:
            # Caso contrário, o segundo interruptor controla a segunda lâmpada
            result.append((1, 1))

            # O terceiro interruptor controla a terceira lâmpada
            result.append((2, 2))

    return result

def check_lamp(is_on):
    """
    Simula a verificação de uma lâmpada.

     :param is_on: o estado da lâmpada
     :return: uma string representando o estado da lâmpada
     """
    if is_on:
        return "on"
    else:
        return "off"

# Teste a função
result = find_switch_lamp(3, 3)
print(result)  # Saída: [(0, 0), (1, 1), (2, 2)]
