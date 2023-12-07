from Operadores import Operadores
calculadora = Operadores()
class Main:
    # Crear una instancia de la clase operadores
    

    while True:
        print("1-Suma")
        print("2-Resta")
        print("3-Multiplicación")
        print("4-División")
        print("5-Salir")
        opcion = input ("Elige la operación que desees: ")
        
        if opcion == "1" :
            num1 = float(input ("Escribe el primer numero a sumar: "))
            num2 = float(input ("Escribe el segundo numero a sumar: "))
            resultado = calculadora.suma(num1,num2)
            print("El resultado es: ", resultado )

        elif opcion == "2":
            num1 = float(input ("Escribe el minuendo: "))
            num2 = float(input ("Escribe el sustrayendo: ")) 
            resultado = calculadora.resta(num1,num2)
            print("El resultado es: ", resultado)    

        elif opcion == "3":
            num1 = float(input ("Escribe el primer factor: "))
            num2 = float(input ("Escribe el segundo factor: ")) 
            resultado = calculadora.multiplicacion(num1,num2)
            print("El producto es: ", resultado)  

        elif opcion == "4":
            num1 = float(input ("Escribe el dividendo: "))
            num2 = float(input ("Escribe el divisor: ")) 
            resultado = calculadora.division(num1,num2)
            print("El cociente es: ", resultado)  

        elif opcion== "5":
            print("Saliendo del programa")
            break

        
