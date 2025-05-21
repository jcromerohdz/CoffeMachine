# REQUERIMIENTOS PARA EL SISTEMA DE INFORMACION DE UNA MAQUINA DE CAFE

1. Pregunte al usuario "¿Qué desea? (espresso/latte/cappuccino):"

	a. Verifique la entrada del usuario para decidir qué hacer a continuación.

	b. El mensaje debe aparecer cada vez que se complete una acción, por ejemplo, 	al servir la bebida. El mensaje debe aparecer de nuevo para atender al 		siguiente cliente.

2. Apague la cafetera escribiendo "off" en el mensaje.

	a. Los encargados del mantenimiento de la cafetera pueden usar "off" como 	palabra secreta para apagarla. Su código debería finalizar la ejecución 	cuando esto ocurra.

3. Imprimir informe.

	a. Cuando el usuario introduce "informe" en la solicitud, se generará un 	informe que muestra los valores actuales de los recursos. Por ejemplo:
	Agua: 100 ml
	Leche: 50 ml
	Café: 76 g
	Dinero: $2.5

4. ¿Comprobar si hay suficientes recursos?	
	a. Cuando el usuario elige una bebida, el programa debe comprobar si hay 	suficientes recursos para prepararla.
	b. Por ejemplo, si un café con leche requiere 200 ml de agua, pero solo 	quedan 100 ml en la máquina, no debe continuar preparándola, sino que debe 	imprimir: "Lo sentimos, no hay suficiente agua".

	c. Lo mismo debe ocurrir si se agota otro recurso, por ejemplo, la leche o el 	café.

5. Procesar monedas.
	a. Si hay suficientes recursos para preparar la bebida seleccionada, el 	programa debería pedirle al usuario que inserte monedas.

	b. Recuerde que las monedas de 25 centavos = $0.25, las de 10 centavos = 	$0.10, las de 5 centavos = $0.05, las de un centavo = $0.01.

	c. Calcule el valor monetario de las monedas insertadas. Por ejemplo, 1 	moneda de 25 centavos, 2 de 10 centavos, 1 de 5 centavos, 2 de un centavo = 	0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52.

6. ¿Verificar si la transacción fue exitosa?
    a. Verificar que el usuario haya ingresado suficiente dinero para comprar la bebida seleccionada. Por ejemplo, un café con leche cuesta $2.50, pero solo se ingresaron $0.52. Después de contar las monedas, el programa debería decir "Lo siento, no hay suficiente dinero. Se reembolsó el dinero".
    b. Si el usuario ha ingresado suficiente dinero, el costo de la bebida se suma a la máquina como ganancia y esto se reflejará la próxima vez que se active el "informe". Por ejemplo, Agua: 100 ml
    Leche: 50 ml
    Café: 76 g
    Dinero: $2.5
    c. Si el usuario ha ingresado demasiado dinero, la máquina debería ofrecer cambio.
    Por ejemplo, "Aquí tiene $2.45 de cambio". El cambio debe redondearse a dos decimales.

7. Preparar café.
    a. Si la transacción es exitosa y hay suficientes recursos para preparar la bebida que el usuario seleccionó, los ingredientes se deducirán de los recursos de la máquina de café.
    Por ejemplo, informe antes de comprar un café con leche: Agua: 300 ml
    Leche: 200 ml
    Café: 100 g
    Dinero: $0
    Informe después de comprar un café con leche:
    Agua: 100 ml
    Leche: 50 ml
    Café: 76 g
    Dinero: $2.5
    b. Una vez deducidos todos los recursos, diga al usuario: "¡Aquí está su café con leche! ¡Disfrútelo!". Si eligió café con leche.