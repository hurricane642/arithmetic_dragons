# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        answer = input(message)
        if answer == 'да' or answer == 'нет' or ',' in answer:
            return answer
        try:
            answer = int(answer)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        if dragon!=RedTroll and dragon!=GreenTroll:
            print('Вышел', dragon._color, 'дракон!')
        else:
            print('Вышел',dragon._color, 'тролль!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** враг кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Враг', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами  и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 5
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 5)
        print('У Вас на пути', dragon_number, 'драконов и троллей')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
