import random
import numpy as np
import datetime

fecha_actual=datetime.datetime.now()

matriz_locales=["bienestarAnimal","supergroom","entrePatas","petcory","buycan","pharmavet"]
matriz1=["canbo naranja cordero","canbo verde cordero","canbo naranja cordero","canbo verde cordero","canbo rosado cordero"
         ,"canbo celeste cordero","canbo verde pollo","canbo azul pollo"
         ,"canbo naranja pollo","canbo morado pollo","canbo senior",
         "canbo skin protection","canbo high balanced","canbo gatos verde",
         "canbo gatos esterilizados","canbo gatos urinary"]
matriz2=["biscuits","lata"]

if(fecha_actual.strftime('%A')=="Sunday"):
    matriz_Locales_Modificado=["petcory"]
else:
    matriz_Locales_Modificado=matriz_locales

productos_mostrados = set()
productos_no_mostrados_max=3

print(f"Ventas {fecha_actual.day}-{fecha_actual.month}-{fecha_actual.year}")


for i in matriz_Locales_Modificado:
        ventas_a_realizar = 5 if i in ["bienestarAnimal", "supergroom"] else 3
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
    
print("________________________________")
print("Productos que no fueron sorteados:")
for producto in productos_no_mostrados:
    print(producto)