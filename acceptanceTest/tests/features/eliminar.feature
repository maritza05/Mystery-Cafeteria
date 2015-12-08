Feature: Eliminar cliente
	Con el fin de tener control de los clientes actuales
	Como empleado registrado 
	Quiero eliminar un cliente.

Scenario: Eliminar cliente existente 
	Dado que el cliente "Vanessa Alcalá" se encuentra registrado en el sistema
	Cuando hago clic en el boton eliminar cliente
	Entonces debo ser capaz de ver la lista con los clientes