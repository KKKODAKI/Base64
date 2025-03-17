
def encode(palavra):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    letras = [] 
    letras_bin = ''
    nova_letra = ''
    encoded = ''

    # Pega a palavra e transoforma cada letra em binario e salva no vetor letras
    for i in range(len(palavra)):

        letras = format(ord(palavra[i]), 'b')

        # Como ele converte para um binario de 7 caracteres
        # Nesse if caso o binario das letras esteja com 8 caracteres está certo
        if (len(letras)==8):
            letras_bin = letras_bin + letras
        # Caso ele tenha 7 caracteres eu adiciono um 0 na frente
        else:
            letras_bin = letras_bin + '0' + letras
        # Todos os binários são colocados na variavel letras bin

    # Aqui eu crio essa variavel letras_bin_mod, pois eu vou usar lá em baixo o tamanho original da string de letras_bin
    letras_bin_mod = letras_bin

    # Caso o tamanho de letras_bi_mod seja multiplo de 6, td certo
    # se não eu adiciono zeros no final até o tamanho ser multiplo de 6
    while(len(letras_bin_mod) % 6 != 0):
        letras_bin_mod = letras_bin_mod + '0'

    # Inicializo a variavel i=1 para usar na lógica mais abaixo
    i = 1

    # Aqui nesse for eu vou pegar a variavel que tem todos o binários das letras e separa-los em 6 caracteres
    for j in range(len(letras_bin_mod)):
        nova_letra = nova_letra + letras_bin_mod[j]

        # Sempre que i passa pelo for eu adiciono +1, quando i=6 ele entra dentro do if a variavel nova_letra está com 6 caracteres
        if(i == 6):
            
            # Aqui eu pego uma variavel encoded e uso uma variavel que eu salvei todas as letras do alfabeto na ordem
            # Nessa função int eu tranformo a nova_letra que estava em binário, em um número decimal
            # E esse número decinal é usado como indice da string, assim sendo igual uma letra
            encoded = encoded + base64_chars[int(nova_letra,2)]
            # i=0 e nova_letra = '' para começar de novo o processo de criar uma nova_letra com 6 caracteres
            i = 0
            nova_letra = ''

        i = i + 1

    # Aqui eu uso o tamnaho original da string letras_bin
    # Caso o resto da divisão por 3 seja 1, adiciona um = no fim da palavra codificada
    if(len(letras_bin)%3==1):
        encoded = encoded + '='
    # Caso o resto da divisão por 3 seja 2, adiciona dois = no fim da palavra codificada    
    elif(len(letras_bin)%3==2):
        encoded = encoded + '=='

    return encoded