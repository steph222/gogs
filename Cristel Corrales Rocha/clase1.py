''''
print("hola mundo")
input("digite su nombre: ")
nombre = ""
edad = 0
estatura = 0.0
esPar = True

nombre=input("Digite su nombre: ")
edad=int(input("Digite su edad: "))
estatura=float(input("Digite su estatura: "))
esPar=bool(int(input("Digite 1 si su edad es Par, o 0 si su edad es Impar: ")))
print("Mi nombre es:",nombre,"tengo" , edad, "años, y mido: ", estatura)
print("Mi nombre es: "+nombre+"tengo",edad+50)
print(f"Mi nombre es: {nombre} tengo {edad} años, y mido: {estatura} m")
'''
'''
#ejercicio 1#
num1=int(input("Digite un primer numero: "))
num2=int(input("Digite un segundo numero: "))

print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}*{num2}={num1*num2}")
'''
num1=int(input("Digite un primer numero: "))
num2=int(input("Digite un segundo numero: "))
suma=num1+num2
print(f"{num1}+{num2}={suma}")
multi=num1*num2
resultadomulti=suma*multi
print(f"{num1}*{num2}={multi}")
print(resultadomulti)