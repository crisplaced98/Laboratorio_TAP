from Lab2.generics.Thing import Thing
class UseThing:
    cosa = Thing(str("Pedro"))
    nombre = cosa.nombre
    print(nombre)

    #En Java esto no se puede realizar ya que ya se ha creado previamente el objeto y, por tanto, ya no es genérico. Sin embargo,
    #en Python hay asignación dinámica y por eso no es un asignación Ilegal
    cosa.nombre = int(7)
    print(cosa.nombre)