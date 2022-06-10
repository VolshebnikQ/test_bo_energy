#   Есть группа из 100 предметов. 
#   Предметы могут быть синего, зелёного и красного цвета. 
#   Известно, что предметов синего цвета сильно больше, чем 
#   предметов зелёного цвета, а предметов зелёного цвета немного больше, 
#   чем предметов красного цвета. Напишите сервис, который будет принимать 
#   номер предмета и пытаться угадать его цвет. Логику работы сервиса определите самостоятельно.

#   i = 100
#   blue_i >> green_i       blue_i = green_i*n + const1
#   green_i > red_i         blue_i = red_i + const2

import random
from random import randint


def suggest_quantity():
    count_item = {
            "ГОЛУБОГО": False,
            "ЗЕЛЁНОГО": False,
            "КРАСНОГО": False,
    }

    n = randint(1,10)

    for i in range(round(100/n)):
        red = i + randint(0,round(100/n))
        green = red + randint(0,round(100/n))
        blue = 100 - green - red
        if 2*red > green and red != green and green*n < blue:
            count_item["КРАСНОГО"], count_item["ЗЕЛЁНОГО"], count_item["ГОЛУБОГО"] = red, green, blue

    if not count_item["КРАСНОГО"]:
        return suggest_quantity()
    else:
        return count_item

def suggest_color(n):
    try:
        n = int(n)
    except ValueError:
        return "Необходимо ввести целое число"

    if not n < 101 or not n > 1:
        return "Необходимо ввести число от 1 до 100"

    count_item = suggest_quantity()
    items = suggest_quantity()

    dirichlet_bag = []
    for i in range(1,101):
        variants = []
        for i in count_item:
            if count_item[i] != 0:
                variants.append(i)
        variant = random.choice(variants)
        count_item[variant] -= 1
        dirichlet_bag.append(variant)
    
    dirichlet_bag = sorted(dirichlet_bag, key=lambda A: random.random())
    return f'''Вы вытащили предмет <b>{dirichlet_bag[n-1]}</b> цвета, в то время как в мешке Дирихле было:
            <br>{items["КРАСНОГО"]} - красного цвета
            <br>{items["ЗЕЛЁНОГО"]} - зелёного цвета
            <br>{items["ГОЛУБОГО"]} - голубого цвета'''