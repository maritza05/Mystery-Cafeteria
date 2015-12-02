Feature: Eliminar cliente
Con el fin de tener control de los clientes actuales
Como empleado registrado 
Quiero eliminar un cliente.

Scenario: Eliminar cliente existente 
	Dado que el cliente "Vanessa Alcalá" se encuentra registrado en el sistema
	Cuando hago clic en eliminar
	Entonces debería ser capaz de ver un mensaje con "Cliente eliminado Exitosamente"

Scenario: Eliminar un cliente no existenete
	Dado que el cliente "Vanessa Alcalá" no se encuentra registrado.
	Cuando hago clic en eliminar
	Entonces debería ser capaz de ver un mensaje con "El cliente no existe".