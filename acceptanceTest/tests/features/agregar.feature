Feature: Agregar clientes nuevos
	Con el fin de poder tener más clientes
	Como un cliente
	Quiero agregar nuevos clientes.

Scenario: Agregar cliente exitosamente
	Given que me encuentro en la pagina principal como cliente
	When hago clic en el boton nuevo cliente
	Then debo ser capaz de ver un mensaje "CL-001:Vanessa Alcalá agregado exitosamente"

Scenario: Agegar un cliente ya existente 
	Dado que me encuentro en la pagina principal como cliente
	Cuando hago clic en el boton nuevo cliente 
	Entonces debo ser capaz de ver el mensaje "Cliente ya registrado, por favor introduce información nueva"