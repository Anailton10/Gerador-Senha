from string import digits, punctuation, ascii_letters
from random import sample
from colorama import Fore
letras = ascii_letters
numeros = digits
caracteres = punctuation
senha = letras + numeros + caracteres
gerar = sample(senha, 8)
print('Sua senha forte é: ', end='')
for x in gerar:
    print(Fore.GREEN + ''.join(x) + Fore.RESET, end=' ')

