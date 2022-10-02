
def Den_nedeli():
    a = int(input('Введите день недели: '))
    if (a == 1 or a == 2 or a == 3 or a == 4 or a ==5):
        print('Это рабочий день')
    elif (a ==6 or a ==7):
        print ('Это выходной')
    else:
        print ('Введите число от 1 до 7')



def Istina():
    x = 3
    y = 4
    z = -8
    first_value = not (x or y or z)
    second_value = not x and not y and not z
    ansver = first_value == second_value
    print (ansver)


    
def Opredelenie_chetverti_osi():
    koordinata_x = int(input('Введите координату Х: '))
    koordinata_y = int(input('Введите координату У: '))
    if (koordinata_x == 0 or koordinata_y == 0):
        print('Координаты Х и У не должны равняться нулю!')
    elif (koordinata_x > 0 and koordinata_y > 0):
        print('Первая четверть')
    elif (koordinata_x < 0 and koordinata_y > 0):
        print('Вторая четверть')
    elif (koordinata_x < 0 and koordinata_y < 0):
        print('Третья четверть')  
    elif (koordinata_x > 0 and koordinata_y < 0):
        print('Четвертая четверть')  
    else:
        print('Введите допустимые значения!')


def Opredelenie_diapazona():
    value = int(input('Введите четверть: '))
    if (value == 1):
        print('x > 0 and y > 0')
    elif (value == 2):
        print('x < 0 and y > 0')
    elif (value == 3):
        print('x < 0 and y < 0')
    elif (value == 4):
        print('x > 0 and y < 0')    
    else:
        print('Введите допустимые значения!')


def Rasstoyanie_in_2d():
    point_1x = int(input('Введите x первой точки: '))
    point_1y = int(input('Введите y первой точки: '))
    point_2x = int(input('Введите x второй точки: '))
    point_2y = int(input('Введите y второй точки: '))

    ab = ((point_2x - point_1x)**2 + (point_2y - point_1y)**2)**0.5
    print(ab)

# Den_nedeli()
# Istina()
# Opredelenie_chetverti_osi()
# Opredelenie_diapazona()
# Rasstoyanie_in_2d()