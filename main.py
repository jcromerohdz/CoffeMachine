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
        },
        "costo": 3.0,
    }
}

ganancia = 0
recursos = {
    "agua": 4000,
    "leche": 200,
    "cafe": 100
}

def hay_recurso_suficiente(ingredientes_orden):
    """Retorna True cuando la orden pude ser producida o False si no hay suficientes recursos"""
    es_suficiente = True
    for i in ingredientes_orden:
        if ingredientes_orden[i] >= recursos[i]:
            print(f"Lo sentimos no podemos hacer tu bebida por falta de {i}!")
            es_suficiente = False
    return es_suficiente

def proceso_monedas():
    """Retorna el valor calculado de las monedas insertadas"""
    print("Por favor inserte las monedas....")
    total = int(input("¿ Cuantas monedas de $25c ?: ")) * 0.25
    total += int(input("¿ Cuantas monedas de $10c ?: ")) * 0.10
    total += int(input("¿ Cuantas monedas de $5c ?: ")) * 0.05
    total += int(input("¿ Cuantas monedas de $1c ?: ")) * 0.01
    return total

def transaccion_exitosa(pago, costo_bebida):
    """Retorna True cuando el pago se hizo exitosamente, o False cuando el pago no ha sido suficiente"""
    if pago >= costo_bebida:
        cambio = round(pago - costo_bebida, 2)
        print(f'Aqui tienes tu cambio ${cambio}')
        global ganancia
        ganancia += costo_bebida
        return True
    else:
        print("Lo lamentamos el pago no es suficiente. Te regrasamos tu pago actual!")
        return False

def hacer_cafe(nombre_bebida, ingredientes):
    """Deducir los ingredientes requeridos de los recursos"""
    for ingrediente in ingredientes:
        recursos[ingrediente] -= ingredientes[ingrediente]

    print(f"Aquí tienes tu café {nombre_bebida} ☕")

switch = True

while switch:
    eleccion = input("¿Que le gustaria tomar el dia de hoy? (espresso, latte, cappucciono): ")

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
    elif eleccion == "latte" or eleccion == "espresso" or eleccion == "cappucciono":
        bebida = MENU[eleccion]
        if hay_recurso_suficiente(bebida["ingredientes"]):
            pago = proceso_monedas()
            if transaccion_exitosa(pago, bebida["costo"]):
                hacer_cafe(eleccion, bebida["ingredientes"])
    else:
        print("Lo sentimos no tenemos esa opcion por el momento!")