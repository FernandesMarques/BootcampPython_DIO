#A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.
C = int(input()) 
for i in range (C): 
  N = int(input())
  if N > 8000:
    print("Mais de 8000!")
  else:
    print("Inseto!")
