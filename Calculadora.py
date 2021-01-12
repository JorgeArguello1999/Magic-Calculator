###Caligrafias
Calculadora_Temperatura = ("""  _____      _            _           _                       _      
 / ____|    | |          | |         | |                     | |     
| |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _    __| | ___ 
| |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |  / _` |/ _ \
| |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | | (_| |  __/
 \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|  \__,_|\___|
                                                                     
                                                                     
 _______                                  _                   
|__   __|                                | |                  
   | | ___ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ __ _ 
   | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _` |
   | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | | (_| |
   |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \__,_|
                    | |                                       
                    |_|                                     """)




Separador = "#############################################################################################################################################################\n"


print("""
    
  /$$$$$$            /$$                     /$$                 /$$                             
 /$$__  $$          | $$                    | $$                | $$                             
| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$ 
| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$
| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$| $$  | $$| $$  \ $$| $$  \__/ /$$$$$$$
| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$      /$$__  $$
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$
 \______/  \_______/|__/ \_______/ \______/ |__/ \_______/ \_______/ \______/ |__/      \_______/
                                                                                                 
                                                                                                 
                                                                                                 
  /$$$$$$                          /$$                                                           
 /$$__  $$                        |__/                                                           
| $$  \ $$ /$$   /$$ /$$$$$$/$$$$  /$$  /$$$$$$$  /$$$$$$                                        
| $$  | $$| $$  | $$| $$_  $$_  $$| $$ /$$_____/ |____  $$                                       
| $$  | $$| $$  | $$| $$ \ $$ \ $$| $$| $$        /$$$$$$$                                       
| $$/$$ $$| $$  | $$| $$ | $$ | $$| $$| $$       /$$__  $$                                       
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$|  $$$$$$$|  $$$$$$$                                       
 \____ $$$ \______/ |__/ |__/ |__/|__/ \_______/ \_______/                                       
      \__/                                                                                       
                                                                                                 
""")

###Definir que quiere hacer el usuario
    
opciones = float(input('Calculadora de Temperatura =     ("0")\nCalculadora de Longitud    =     ("1")\nCual eliges________________=     '))

print(Separador)

###Calculadora de Temperatura
###Ya acabe con las conversiones de temperatura 
while opciones <= 2:

    if opciones == 0:
       
        print (Calculadora_Temperatura)
        opcionesTemperatura = int(input('Convertir: ºF a ºC___________("0")\nConvertir: ºC a ºF___________("1")\nConvertir: ºF a ºK___________("2")\nConvertir: ºK a ºF___________("3")\nConvertir: '))
        print (Separador)

        while opcionesTemperatura <= 3:
            if opcionesTemperatura == 0:

                F= float(input("Fahrenheit_a_Celsius..."))
                C= (F-32)/18
                print (C)

                break

            elif opcionesTemperatura == 1:
               
                C = float(input("Celsius_a_Fahrenheit: "))
                F = (1.8*C) + 32
                print (F)
                
                break

            elif opcionesTemperatura == 2:

                F = float(input("Fahrenheit_a_Kelvin: "))
                K = (F + 459.67)/1.8
                print (K)

                break

            elif opcionesTemperatura == 3:

                K = float(input("Kelvin_a_Fahrenheit: "))
                F = (9/5)*K - 459.67
                print(F)

                break

        break

    elif opciones == 1:
       
        print ("Calculadora de Longitud")
        
        break

    else:
       
        print ("Chao...")
