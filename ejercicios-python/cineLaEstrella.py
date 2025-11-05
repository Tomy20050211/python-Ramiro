
edadCliente = int(input("Ingresa tu edad: "))
  
if edadCliente <= 0:
        print()

elif edadCliente < 5:
        print("Tu entrada es gratis :D")

elif  5 <= edadCliente <= 11:
        print("Tu entrada cuenta $5.000")

elif 12 <= edadCliente <= 59:
        print("Tu entrada cuesta $8.000")

else:
        print("Tu entrada cuesta 4.000 (descuento adulto mayor)")
