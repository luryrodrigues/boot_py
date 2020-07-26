import random
import draw
list_of_words=['BANANA','ABACATE','PYTHON','BOOTCAMP','QUIMICA','FILME','MUSICA','CACHORRO','LINKEDIN','ALMOFADA']

def choose_word():
    word=random.choice(list_of_words)
    return word

def play(word):
    blank='_ '*len(word)
    list_of_blank=list(blank.split())
    letters_in_word=list(word)
    guessed_letters=[]
    attempt=6
    hit=False
    print('=-'*28)
    print('VAMOS JOGAR FORCA?')
    print('Você terá que adivinhar a palavra que pensei! VAMOS LÁ?')
    print('=-'*28)
    print (draw.draw(attempt))
    print(blank)
    while not hit and attempt > 0:
        guess=input('Tente adivinhar uma letra ou palavra: ').strip().upper()
        if len(guess)==1 and guess.isalpha():
            if guess in word:
                guessed_letters.append(guess)
                print(f'Você acertou! A palavra tem letra {guess}.')
                for i in range(0,len(word)):
                    if letters_in_word[i]==guess:
                        list_of_blank[i] = guess
                        blank=''.join(list_of_blank)
                print (draw.draw(attempt))
                print(blank)
                if '_' not in list_of_blank:
                    print(f"PARABÉNS!! Você ganhou o jogo! A palavra era {word}.")
                    hit=True
            elif guess in guessed_letters:
                print(f'Você já tentou a letra {guess} antes. Tente outra!')
                print (draw.draw(attempt))
                print(blank)
            else:
                print(f'Não tem a letra {guess} na palavra. Que pena!')
                guessed_letters.append(guess)
                attempt-=1
                print(draw.draw(attempt))
                print(blank)
        if len(guess)!=1:
            if guess==word:
                print(f"PARABÉNS!! Você ganhou o jogo! A palavra era {word}.")
                hit=True
            else:
                print(f'GAME OVER! Não foi dessa vez! A palavra era {word}.')
                hit=True
        if attempt==0:
            print(f'Você foi ENFORCADO! A palavra era {word}.')
            hit=True

def main():
    word=choose_word()
    play(word)
    while input('Para jogar novamente digite 1, ou digite qualquer outra tecla para sair: ') == '1':
        word=choose_word()
        play(word)
if __name__=='__main__':
    main()