from enum import Enum


class Season(Enum):
    WINTER = 'WINTER'
    SUMMER = 'SUMMER'
    SPRING = 'SPRING'
    FALL = 'FALL'

temporada = Season.SUMMER
if temporada is Season.SUMMER:
    print('Verano')
elif temporada is Season.WINTER:
    print('Invierno')
elif temporada is Season.FALL:
    print('Otoño')
elif temporada is Season.SPRING:
    print('Primavera')

lista = list(map(lambda x: x.value, Season._member_map_.values()))
print(lista)