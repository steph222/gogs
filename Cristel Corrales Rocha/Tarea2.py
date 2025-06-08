#promedio escolar

nombre= input("Sacaremos la nota de su promedio anual, por favor primero ingrese su nombre completo: ")
nota1 = int(input("Ingrese la nota de su primer examen: "))
nota2 = int(input("Ingrese la nota de su segundo examen: "))
nota3 = int(input("Ingrese la nota de su tercer examen: "))

promedio = (nota1 + nota2 + nota3 ) / 3

print("\nSu promedio anual es de : ", round(promedio, 2))

if promedio >=70:
    print(f"Felicitaciones {nombre} usted ha aprovado el año ")
elif 60 <= promedio < 70:
    print(f"{nombre} su nota no es sufiente para aprovar, deberá presentarse a convocatoria")
else:
    print(f"Lo sentimos {nombre}usted no ha aprovado el año")


          