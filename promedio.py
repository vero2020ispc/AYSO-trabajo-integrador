#Programa para el Trabjo Integrador de Arquitectura y Sistemas Operativos.
#El programa solicitará al usuario 3 números y calculará el promedio

#desarrollo del programa, se solicita al usuario los números:
print("¡Bienvenido!")
print("Este programa calcula el promedio entre 3 números dados")

#se define la variable cant_numeros porque es más fácil de modificar.
#Si a futuro se quiere calcular el promedio de más números (o menos) sólo se modifica
#el valor en esta variable, el resto del programa igual funcionaría.
cant_numeros = 3
suma = 0

#se utiliza un ciclo for para solicitar al usuario los números y sumarlos
for cont in range (1, cant_numeros+1):
    print("Ingrese el número",(cont)) #le indica al usuario el orden del número que está ingresando
    num = int(input())
    suma = suma + num

#con round se redondea el resultado para que sólo muestre 2 decimales, mejora la visual
print(f"El promedio de los valores ingresados es {round(suma/cant_numeros,2)}")