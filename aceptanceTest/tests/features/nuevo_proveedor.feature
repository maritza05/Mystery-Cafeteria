Feature: Agrego nuevo proveedor
    Con el fin de poder ofrecer una gran variedad de productos
    Como empleado registrado
    Quiero agregar un nuevo proveedor

Scenario: Crear proveedor
	Given Que me encuentro en la pagina principal como empleado
	When Oprimo el botón de nuevo proveedor
	Then Puedo ver el mensaje "Nuevo proveedor"