import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def jogar():
    print('Jokenpô! 🪨 📃✂️')
    # emoji = [pedra, papel, tesoura]
    emoji = ['🪨', '📃', '✂️']

    while True:
        escolha = int(input('Qual você escolhe? Digite 0 para pedra, 1 para papel ou 2 para tesoura.\n'))
        escolha_pc = random.randint(0, 2)

        if escolha not in [0, 1, 2]:
            print('Escolha inválida, tente novamente!')
            continue
        else:
            if escolha == escolha_pc:
                print(f'Você escolheu:\n{emoji[escolha]}\nO computador escolheu:\n{emoji[escolha_pc]}\nEmpate! 🙅')
            elif escolha == 0 and escolha_pc == 2:
                print(f'Você escolheu:\n{emoji[escolha]}\nO computador escolheu:\n{emoji[escolha_pc]}\nVocê ganhou! 🏆')
            elif escolha == 2 and escolha_pc == 0:
                print(f'Você escolheu:\n{emoji[escolha]}\nO computador escolheu:\n{emoji[escolha_pc]}\nVocê perdeu! 🥈')
            elif escolha > escolha_pc:
                print(f'Você escolheu:\n{emoji[escolha]}\nO computador escolheu:\n{emoji[escolha_pc]}\nVocê ganhou! 🏆')
            elif escolha < escolha_pc:
                print(f'Você escolheu:\n{emoji[escolha]}\nO computador escolheu:\n{emoji[escolha_pc]}\nVocê perdeu! 🥈')
            break

while True:
    jogar()
    replay = input('Você quer jogar de novo? (S/N): ').lower()
    if replay != 's':
        print('Obrigado por jogar! Adeus!')
        break