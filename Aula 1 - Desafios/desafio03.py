N = int(input())
lista = []
i = 0
while(N > 0):
    a = input()
    b = input()
    if b == a[len(a)-len(b):len(a)]:
        print('encaixa')
    else:
        print('nao encaixa')
    
    N=N-1
    
