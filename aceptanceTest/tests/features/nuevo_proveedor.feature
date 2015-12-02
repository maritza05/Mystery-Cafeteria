Feature: Agrego nuevo proveedor
    Con el fin de poder ofrecer una gran variedad de productos
    Como empleado registrado
    Quiero agregar un nuevo proveedor

Scenario: Ver nuevo proveedor exitosamente
	Given Que he ingresado como "Maritza"
	When Oprimo el botón de nuevo proveedor
	Then Puedo ver el mensaje "Nuevo proveedor"

Scenario: Crear nuevo proveedor exitosamente
	Given Que he ingresado como "Maritza" y me encuentro en nuevo proveedor
	When Introduzco los datos "Postres fríos", "Quebradilla 125" AND Hago clic el botón guardar
	Then Puedo ver el mensaje "Proveedor creado exitosamente"

Scenario: Crear nuevo proveedor sin exito
	Given Que he ingresado como "Maritza" y me encuentro en nuevo proveedor
	When Introduzco los datos "", "" AND Hago clic el botón guardar
	Then Puedo ver el mensaje "Por favor introduce la informacion del proveedor"
