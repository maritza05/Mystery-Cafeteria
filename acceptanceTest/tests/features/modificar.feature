Feature: Modificar Clientes
	Con el fin de poder actualizar la información de un cliente
	Como empleado registrado 
	Quiero modificar los clientes

Scenario: Modificar cliente exitosamente
	Given que el cliente "Vanessa Alcalá" se encuentra registrado AND me encuentro en la pantalla de editar
	When cambio el nombre por "Alejandra Alcalá" AND hago clic en el boton de modificar
	Then puedo ver en la lista actualizada de clientes con el cliente "Alejandra Alcalá"
