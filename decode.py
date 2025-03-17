def decode(encoded):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    letras_encoded = []
    letras_bin = ''
    nova_letra = ''
    palavra = ''
    
    for i in range(len(encoded)):

        letras_encoded = bin(base64_chars.find(encoded[i]))
        letras_encoded = letras_encoded[2:]

        while(len(letras_encoded) != 6):
            letras_encoded = '0' + letras_encoded

        letras_bin = letras_bin + letras_encoded

    print(letras_bin)

    i=1

    for j in range(len(letras_bin)):
        nova_letra = nova_letra + letras_bin[j]

        if(i == 8):
            
            palavra = palavra + chr(int(int(nova_letra,2)))
        
            i = 0
            nova_letra = ''

        i = i + 1

    return palavra

encoded = 'TWFu'

palavra = decode(encoded)

print(palavra)