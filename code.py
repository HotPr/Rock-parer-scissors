import random
import time


while True:



    param = [
        'камень',
        'бумага' ,
        'ножницы'
        ]

    
    draw = ['Ничья!' , 'Никто не выиграл!']
    win_player = ['Вы победили!', 'Компьютер проиграл!', 'Ты выиграл!']
    
    lose_player = [
        'Вас выиграл компьютер!',
        'Победил компьютер',
        'Вы лооооооох!',
        'Вас обыграла машина!'
        ]

    print('Добро пожаловать в камень, ножницы, бумага!') #добавить время на выбор
    time.sleep(1)
    print('Что ты выберешь: камень, ножницы или бумага?') #можно сделать рандомный текст победы

    people_answear = input()


    time.sleep(0.5)
    print('Компьютер выбирает свой ответ...')
    time.sleep(1)
    print('...')

    comp_answear = random.choice(param)



    if people_answear == comp_answear:
        print(random.choice(draw))
        print('Компьютер тоже выбрал:', comp_answear)
    elif people_answear == 'бумага':
        if comp_answear == 'ножницы':
            print(random.choice(lose_player))
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'камень':
            print(random.choice(win_player))
            print('Компьютер выбрал:', comp_answear)
    elif people_answear == 'ножницы':
        if comp_answear == 'камень':
            print(random.choice(lose_player))
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'бумага':
            print(random.choice(win_player))
            print('Компьютер выбрал:', comp_answear)
    elif people_answear == 'камень':
        if comp_answear == 'бумага':
            print(random.choice(lose_player))
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'ножницы':
            print(random.choice(win_player))
            print('Компьютер выбрал:', comp_answear)
    else:
        print("Ошибка, вы не выбрали камень, ножницы или бумагу")
    
    print("\nВы хотите продолжить игру? \nда/нет" )
    end_answear = input()
    if end_answear == 'да':
        print('Окей, продолжаем!')
        print('\n -------------------- \n')
    elif end_answear == 'нет':
        print('Печалька, до скорой встречи!')
        break
    else:
        print('Вы не ответили, поэтому мини-игра будет закрыта через 5 секунд')
        time.sleep(5)
        break

        
    
