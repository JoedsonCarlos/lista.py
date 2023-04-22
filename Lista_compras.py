import os

lista=[]

while True:
    print('Digite um dos valores Abaixo')
    recebe=input('Digite [A]apagar,[I]inserir,[L]listar ')
    
    if recebe=='i':
        os.system('clear')
        valor=input('Digite um produto: ')
        lista.append(valor)
    elif recebe=='a':
        os.system('clear')
        ind=input('digite i ndice no qual você quer apagar')
        try:
            indice=int(ind)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro')
        except IndexError:
            print('Este Indice não existe na lista')
        
    elif recebe=='l':
        os.system('clear')
        if len(lista)==0:
            print('sua liata estar vazia')
        for indice,produto in enumerate(lista):
            print(indice, produto)
    else:
        print('digite um valor entre a, i ou l')
            
        
    