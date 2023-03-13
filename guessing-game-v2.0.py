from random import randint
from time import sleep

# seleciona um número aleatoriamente entre 0 e 10
num_computer = randint(0, 10)

print('-=' *20)
print('O computador escolheu um número de 0 a 10')
print('-=' *20)

# entrada para o usuario inserir o seu palpite
num_player = int(input('Insira o seu palpite> '))

# o contador recebe 1 devido o input fora do while que conta como uma tentativa
c = 1

# pra ficar bonitinho
print('Processando...')
sleep(2)

# o programa vai continuar pedindo o palpite até o usário acertar mostrando se o palpite está alto ou baixo
while num_player != num_computer:
    
    if num_player < num_computer:
        num_player = int(input('Muito abaixo. Tente novamente: '))
    else:
        num_player = int(input('Muito acima. Tente novamente: '))

    print('Processando...')
    sleep(1)
    c += 1

# vai analisar se o palpite do usúario confere com o do computador
if num_player == num_computer:
    print('Parabéns, você acertou!')

# vai imprimir a resposta certa e o número de tentativas
print('O número escolhido foi {}'.format(num_computer))
print('Você acertou em {} tentativas.'.format(c))
