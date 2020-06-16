arquivo = open('lista-nomes-maiusc.txt', 'r')
lista_nomes = arquivo.readlines()
arquivo.close()
nomes_arrumados = []

for nome_completo in lista_nomes:
    nome_arrumado = ''
    nomes = nome_completo.split()
    for nome in nomes:
        if (nome == 'DE' or nome == 'DO' or nome == 'DA' 
            or nome == 'DOS' or nome == 'DAS' or nome == 'E'):
            nome = nome.lower()
        else:
            nome = nome.capitalize()
        nome_arrumado = ' '.join([nome_arrumado, nome])
    nomes_arrumados.append(nome_arrumado)

print(nomes_arrumados)