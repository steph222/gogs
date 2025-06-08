numerosecreto=int("8")
input("Haremos una adivinanza de un numero secreto para ti, preciona enter para continuar")
nombre=input("Digite su nombre y apellido: ")
edad=int(input("Digite su edad: "))
numero_usuario=int(input("Digite un numero de su preferencia:" ))
if(numero_usuario==8):
    mensaje="Usted ha dado con el numero secreto correcto, felicitaciones=)"
else:
    mensaje="Usted ha dado con el numero secreto incorrecto, gracias por el intento"
print(f"{nombre} {mensaje} ")

