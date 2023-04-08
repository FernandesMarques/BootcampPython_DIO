'''DESAFIO: Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.'''

a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if c == ('onivoro'):
            print('homem')
        else:
            print('vaca') 
else: 
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if c == ('hematofago'):
            print('sanguessuga')
        else:
            print('minhoca')     