chocolate = 4000
vainilla = 3500
topping = 1000

print("SABORES")
print("-------")
print("chocolate - $4.000")
print("Vainilla - 3.500")
saborCliente = input("Que sabor de helado quieres? ")

if saborCliente.lower() == "chocolate":
        recioHelado = chocolate

elif saborCliente.lower() == "vainilla":
        precioHelado = vainilla

else:
    print("El sabor no existe en esta tienda...")
    precioHelado = None

if precioHelado is not None:
    opcional = input("Quieres agregarle algun topping? Costo: $1.000 (Si/No)")

    if opcional.lower() == "si":
        precioHelado += topping
        print("VALOR TOTAL")
        print("-----------")
        print(f"${precioHelado}")

    elif opcional.lower() == "no":
        print("VALOR TOTAL")
        print("-----------")
        print(f"${precioHelado}")
    else:
        print("Valor incorrecto, vuelva a hacer la compra")
