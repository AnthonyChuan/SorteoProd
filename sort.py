import random
import numpy as np
import datetime

fecha_actual=datetime.datetime.now()

matriz_locales=["bienestarAnimal","supergroom","entrePatas","petcory"]
matriz1=["canbo naranja cordero","canbo verde cordero","canbo naranja cordero","canbo verde cordero","canbo rosado cordero"
         ,"canbo celeste cordero","canbo verde pollo","canbo azul pollo"
         ,"canbo naranja pollo","canbo morado pollo","canbo senior",
         "canbo skin protection","canbo high balanced","canbo gatos verde",
         "canbo gatos esterilizados","canbo gatos urinary"]
matriz2=["biscuits","cambito"]



productos_mostrados = set()
productos_no_mostrados_max=3

impresion_de_fecha=f"Ventas {fecha_actual.day}-{fecha_actual.month}-{fecha_actual.year}"

if(fecha_actual.strftime('%A')=="Sunday"):
    matriz_Locales_Modificado=["petcory"]
    for i in matriz_Locales_Modificado:
        ventas_a_realizar = 3
    print(impresion_de_fecha)    
    print(f"________________________________\n{i.capitalize()}\n________________________________")
    
    for j in range(ventas_a_realizar):
            print(f"Venta {j+1}")

            productos_a_imprimir = []
            bivalor = random.randint(1, 2)  # Decidimos si habrá 1 o 2 productos en la venta

            while len(productos_a_imprimir) < 1:
                producto_random = random.choice(matriz1)
                if producto_random in ["canbo high balanced", "canbo skin protection", "canbo senior"]:
                    matriz1.remove(producto_random)
                if producto_random not in productos_a_imprimir:
                    productos_a_imprimir.append(producto_random)

            if bivalor == 2:
                productos_a_imprimir.append(random.choice(matriz2))

            # Imprimimos los productos seleccionados
            for producto in productos_a_imprimir:
                print(producto)
                productos_mostrados.add(producto)
else:
    matriz_Locales_Modificado=matriz_locales
    while True:
        print(impresion_de_fecha)
        # Repetir el ciclo hasta que no haya productos no mostrados
        for i in matriz_Locales_Modificado:
            print(f"________________________________\n{i.capitalize()}\n________________________________")
            
            # Definir el número de ventas según el local
            if i == "bienestarAnimal":
                ventas_a_realizar = 10
            elif i == "supergroom":
                ventas_a_realizar = 5
            else:
                ventas_a_realizar = 3

            # Loop de ventas por local
            for j in range(ventas_a_realizar):
                print(f"Venta {j+1}")
                productos_a_imprimir = []

                # Decidir cuántos productos se imprimirán (1 o más)
                cantidad_productos = random.randint(1, 3 if i == "bienestarAnimal" else 1)

                # Selección de productos aleatorios de matriz1
                while len(productos_a_imprimir) < cantidad_productos:
                    producto_random = random.choice(matriz1)
                    if producto_random not in productos_a_imprimir:
                        productos_a_imprimir.append(producto_random)

                # Si se requiere, agregar un producto de matriz2
                if random.randint(1, 2) == 2:
                    productos_a_imprimir.append(random.choice(matriz2))

                # Imprimir productos seleccionados para la venta actual
                for producto in productos_a_imprimir:
                    print(producto)
                    productos_mostrados.add(producto)

        # Calcular productos que no han sido mostrados
        productos_no_mostrados = set(matriz1) - productos_mostrados

        # Verificar si ya no quedan productos no mostrados
        if not productos_no_mostrados:
            print("________________________________")
            print("Todos los productos fueron sorteados al menos una vez.")
            break  # Salir del while si todos los productos han sido mostrados
        else:
            print(f"Productos no mostrados aún: {productos_no_mostrados}")



"""for i in matriz_Locales_Modificado:
        
        if  i == "bienestarAnimal":
            ventas_a_realizar=13
            
        elif i == "supergroom":
            ventas_a_realizar=5
        else:
            ventas_a_realizar=3
            
        print(f"________________________________\n{i.capitalize()}\n________________________________")
        
        for j in range(ventas_a_realizar):
            print(f"Venta {j+1}")
            productos_a_imprimir = []

            # Decidir cuántos productos se imprimirán (1, 2 o 3 para "bienestarAnimal", 1 o 2 para otros)
            triprimer = random.randint(1, 3) if i == "bienestarAnimal" else 1
            bivalor = random.randint(1, 2)

            # Selección de productos aleatorios
            while len(productos_a_imprimir) < triprimer:
                producto_random = random.choice(matriz1)
                # Evitar agregar productos repetidos en la misma venta
                if producto_random not in productos_a_imprimir:
                    productos_a_imprimir.append(producto_random)

            # Si el valor bivalor es 2, agregar un producto extra de matriz2
            if bivalor == 2:
                productos_a_imprimir.append(random.choice(matriz2))

            # Imprimir los productos seleccionados
            for producto in productos_a_imprimir:
                print(producto)
                productos_mostrados.add(producto)
                
        productos_no_mostrados = set(matriz1) - productos_mostrados
        
        
    
print("________________________________")
print("Productos que no fueron sorteados:")
for producto in productos_no_mostrados:
    print(producto)
    
"""    
    
    
    
    
    
    
    
"""ventas_a_realizar = 5 if i in ["bienestarAnimal", "supergroom"] else 3
        print(f"________________________________\n{i.capitalize()}\n________________________________")
    
        for j in range(ventas_a_realizar):
            print(f"Venta {j+1}")

            productos_a_imprimir = []
            bivalor = random.randint(1, 2)  # Decidimos si habrá 1 o 2 productos en la venta

            while len(productos_a_imprimir) < 1:
                producto_random = random.choice(matriz1)
                if producto_random in ["canbo high balanced", "canbo skin protection", "canbo senior"]:
                    matriz1.remove(producto_random)
                if producto_random not in productos_a_imprimir:
                    productos_a_imprimir.append(producto_random)

            if bivalor == 2:
                productos_a_imprimir.append(random.choice(matriz2))

            # Imprimimos los productos seleccionados
            for producto in productos_a_imprimir:
                print(producto)
                productos_mostrados.add(producto)

        productos_no_mostrados = set(matriz1) - productos_mostrados
        """