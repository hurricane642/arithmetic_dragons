# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class GreenTroll(Dragon):
    def __init__(self):
        self._health = 10
        self._attack = 10
        self._color = 'зеленый'

    def question(self):
        x = randint(1,5)
        self.__quest = 'Какое загаданное число?'
        self.set_answer(x)
        return self.__quest
class RedTroll(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
    def isPrime(self, n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2

        return d * d > n

    def question(self):
        x = randint(1,100)
        self.__quest = 'Простое ли число '+ str(x)+' ?'
        if self.isPrime(x):
            self.set_answer('да')
        else:
            self.set_answer('нет')
        return self.__quest
class BlackTroll(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'
    def otvet(self,n):
        a=[]
        d = 2
        if n > 1:
            a.append(n)
        while d * d <= n:
            if n % d == 0:
                a.append(d)
                n //= d
            else:
                d += 1
        b = ''
        for i in a:
            b += str(i)
            b += ','
        b = b[0:-1]
        return b

    def question(self):
        x = randint(1,100)
        self.__quest = 'Разложите число ' + str(x)+ ' на множители!'
        self.set_answer(x)
        return self.__quest


enemy_types = [GreenTroll,RedTroll]
#GreenDragon, RedDragon, BlackDragon,