def inverter_string(string):
    reverso = ''
    for letra in string:
        reverso = letra + reverso
    return reverso


palavra = input("Escreva uma palavra e descubra o seu reverso: ")
print(inverter_string(palavra))