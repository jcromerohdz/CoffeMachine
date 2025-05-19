MENU = {
    "espresso" : {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24
        },
        "costo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24
        }
    }
}

ganancia = 0
recursos = {
    "agua": 4000,
    "leche": 200,
    "cafe": 100
}

def hay_recurso_suficiente(ingredientes_orden):
    es_suficiente = True
    for i in ingredientes_orden:
        if ingredientes_orden[i] >= recursos[i]:
            print(f"Lo sentimos no podemos hacer tu bebida por falta de {i}!")
            es_suficiente = False
    return es_suficiente

switch = True

while switch:
    eleccion = input("¿Que le gustaria? (espresso, latte, cappucciono): ")

    if eleccion == "off":
        print("📴 Apagando Maquina....")
        switch = False
    elif eleccion == "reporte":
        print(f'===========REPORTE DE RECURSOS EN EL ALMACEN===============')
        print(f'Agua : 💧 {recursos["agua"]}ml')
        print(f'Leche 🥛: {recursos["leche"]}ml')
        print(f'Cafe : ☕ {recursos["cafe"]}g')
        print(f'===========REPORTE GANANCIAS===============')
        print(f'Ganancias 💰: {ganancia}')
    else:
        bebida = MENU[eleccion]
        hay_recurso_suficiente(bebida["ingredientes"])


    