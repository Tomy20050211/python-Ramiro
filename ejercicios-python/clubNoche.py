edad = int(input("Ingrese su edad: "))
documento = input("Tiene documento? (si/no): ")

if edad < 18:
    print("Entrada denegada")
elif edad >= 18 and documento == "si":
    print("Entrada permitida")
elif edad >= 18 and documento == "no":
    print("Debe presentar el documento")