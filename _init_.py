#Jose Barrera Ramos
#Ingenieria en Sistemas

from operations import *


def game():
    score = 0
    while True:
        print('========Menu========'
              '\n1.Add'
              '\n2.Resta'
              '\n3.Multiplicacion'
              '\n4.Division'
              '\n5.Potencia'
              '\n0.Exit')
        option = int(input('\nChoice an option:'))

        if option == 0:
            break

        num_1 = int(input('Enter first number:'))
        num_2 = int(input('Enter second number:'))
        answer = int(input('Enter your answer:'))

        if option == 1:
            result = add(num_1, num_2)

        if option == 2:
            result = resta(num_1, num_2)

        if option == 3:
            result = multiplicacion(num_1, num_2)

        if option == 4:
            result = division(num_1, num_2)

        if option == 5:
            result = potencia(num_1, num_2)

        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')

    print(f'========GameOver========'
          f'\nYour score is{score}'
          '\nKeep going!')


game()
