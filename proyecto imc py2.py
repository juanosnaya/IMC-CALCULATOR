personas = int(input("personas: "))
while personas > 0:
    n = input ("Por favor, introduzca su nombre: ")
    e = int(input( "Por favor, introduzca su edad en años: "))
    a = float(input ("Por favor, introduzca su estatura en metros: "))
    est = a
    m = float (input("Por favor, introduzca su peso en kilogramos: "))
    IMC = m / est**2
    if(e < 18):
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
    print("IMC: " + str(IMC))
    if IMC >= 0 and  IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99:
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.99:
        print ("Obesidad media")
    elif IMC >= 40.00:
        print ("Obesidad mórbida")
    personas = personas -1