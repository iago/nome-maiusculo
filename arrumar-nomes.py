arqNomeMaiusc = open('lista-nomes-maiusc.txt', 'r')
listaNomes = arqNomeMaiusc.readlines()
arqNomeMaiusc.close()
nomesArrumados = []

for nomeCompleto in listaNomes:
    nomeArrumado = ''
    nomes = nomeCompleto.split()
    for nome in nomes:
        if (   nome == 'DE' or nome == 'DO' or nome == 'DA' 
               or nome == 'DOS' or nome == 'DAS' or nome == 'E'):
            nome = nome.lower()
        else:
            nome = nome.capitalize()
        nomeArrumado = ' '.join([nomeArrumado, nome])
    nomesArrumados.append(nomeArrumado)

print(nomesArrumados)
