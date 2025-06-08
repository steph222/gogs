#condicionales

#condicional simple

# los mieroles se paga la entrada a mitad de precio
"""5

precio=int(input( "digite el precio de la entrada:"))
dia=int(input("digite el dia en el que se encuentra:\n1.lunes \n2.martes \n3.miercoles \n4.jueves \n5.viernes\n\nsu opinion: "))
#igualdad --
#desigualdad |-
#miercoles == miercoles --> true
if (dia == 3):
    precio=precio/2
    print(f"se hizo una reduccion del precio")
print(f"el precio de la entrada es: {precio}")

"""

#condicion doble --> true false

"""
if (condicion):
    accion
else:
    accion
    """
"""
num=int(input("digite un numero: "))
#<>=
if(num>=0):
    mensaje="positivo"
else:
    mensaje="negativo"
    
print(f"el numero: {num} es un numero {mensaje} ")
    
if(num%2!=0):
    mensaje="impar"
else:
    mensaje="par"
    
print(f"el numero tambien es: {mensaje}")
"""
#pregunte su nombre y luego determine si puede conducir 
# un mensaje llamandole por su nombre y diciendole si puede o no

nombre=input("digite su nombre por favor: ")
edad=int(input("digite su edad: "))
if(edad>=18):
    mensaje="mayor de edad "
else:
    mensaje="menor de edad "
print(f"{nombre} usted es {mensaje}")

licencia=int(input("usted cuenta con licencia?:\n1.si \n2.no \n\nsu opinion: "))
if(edad>=18 and licencia==1):
    MENSAJE="usted puede conducir"
else:
    MENSAJE="usted no puede conducir"
print(f"{nombre} usted es {mensaje} y {MENSAJE}")
