#ciclo repeticion for -> para
# for x in range(3):
#     print(f"se portaron mal el sabado {x}")
    
# contador_nota = 0
# try:
#     cantidad = int(input("ingrese cantidad de notas a promediar"))
#     for x in range(cantidad):
#         nota = float(input(f"ingrese nota {x+1}"))
#         contador_nota = contador_nota + nota
#     promedio = round(contador_nota/cantidad, 1)
#     print(f"el resultado de las {cantidad} notas es: {promedio}")
# except:
#     print("tipo de dato no compatible")
#while -> mientras 
bandera = True
while bandera :
    numero = int(input("ingrese un numero"))
    if numero%2==0 :
        print("puede elegir otro numero!")
    else:
        print("el numero es impar, se acabo el ciclo")
        bandera = False
print("muchas gracias por ocupar esta aplicacion")

a=10
while a >= 10:
    numero =  int(input("ingrese numero"))
print ("baicito")
        
    