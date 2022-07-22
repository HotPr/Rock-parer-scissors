import random
import time


while True:



    param = ['камень', 'бумага' , 'ножницы'] 

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
        print('Ничья!')
        print('Компьютер тоже выбрал:', comp_answear)
    elif people_answear == 'бумага':
        if comp_answear == 'ножницы':
            print('Победил компьютер!')
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'камень':
            print('Вы выиграли!')
            print('Компьютер выбрал:', comp_answear)
    elif people_answear == 'ножницы':
        if comp_answear == 'камень':
            print('Победил компьютер!')
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'бумага':
            print('Вы выиграли!')
            print('Компьютер выбрал:', comp_answear)
    elif people_answear == 'камень':
        if comp_answear == 'бумага':
            print('Победил компьютер!')
            print('Компьютер выбрал:', comp_answear)
        elif comp_answear == 'ножницы':
            print('Вы выиграли!')
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

        
    
