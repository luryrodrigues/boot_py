import random
listapalavras=['ABACATE','PYTHON','BOOTCAMP','QUIMICA','FILME','MUSICA','CACHORRO','LINKEDIN','ALMOFADA','FORABOLSONARO']

print('=-'*28)
print('VAMOS JOGAR FORCA?')
print('Você terá que adivinhar a palavra que pensei! VAMOS LÁ?')
print('=-'*28)

class JogoForca:
    def __init__(self):
        self.palavra=random.choice(listapalavras)
        self.espacos='___ '*len(self.palavra)
    def imprimir():
        print(self.espacos)
        print('A palavra é: ')
print(JogoForca().espacos)