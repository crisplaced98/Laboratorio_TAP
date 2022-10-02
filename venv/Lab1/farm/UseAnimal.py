from Lab1.farm.Animal import Animal
from Lab1.farm.Cat import Cat
from Lab1.farm.Dog import Dog
from Lab1.farm.Parrot import Parrot
from Lab1.farm.MutantParrot import MutantParrot

class UsaAnimal:
    a = Animal(3, 3)
    p = Dog(1, 1, True)
    g = Cat(1, 2)
    l = Parrot (1, 2)
    lM  = MutantParrot(3, 3)

    print(f'Animal: {a.habla()}')
    print(f'Perro: {p.habla()}')
    print(f'Gato: {g.habla()}')
    print(f'Loro: {l.habla()}')
    print(f'Loro mutante: {lM.habla()}')

    #Asignación polimórfica. Esto es posible debido a que Perro es hijo de Animal.
    a = p
    print(f'Animal: {a.habla()}') #Resultado = Pulgas true -> Habla como un Perro (Ligadura dinámica)
    # Asignación polimórfica. Esto es posible debido a que LoroMutante es nieto de Animal.
    a = lM
    print(f'Animal: {a.habla()}')