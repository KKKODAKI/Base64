import encode
import decode
import os

os.system('cls')
print('-------------------')
print('1 -  codificar')
print('2 -  decodificar')
print('-------------------')


resposta = input()

os.system('cls')
if(resposta == '1'):

    palavra = input('Escreva uma palavra para ser codificada: ')

    os.system('cls')

    encoded = encode.encode(palavra)

    print('Palavra original: ' + palavra)
    print('Palavra codificada: ' + encoded + '\n')

elif(resposta == '2'):
    
    encoded = input('Escreva uma palavra para ser decodificada: ')
    
    os.system('cls')

    palavra = decode.decode(encoded)
    
    print('Palavra codificada: ' + encoded)
    print('Palavra original: ' + palavra + '\n')
else:
    exit()
