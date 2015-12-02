Feature: Agregar clientes nuevos
Con el fin de poder tener más clientes
Como un empleado registrado
Quierp agregar nuevos clientes.

Scenario: Agregar cliente exitosamente
	Dado que el cliente "Vanessa Alcalá" no se encuentra registrado
	Cuando hago clic en el botón crear
	Entonces debo ser capaz de ver un mensaje "CL-001:Vanessa Alcalá agregado exitosamente"

Scenario: Agegar un cliente ya existente 
	Dado que el cliente "Vanessa Alcalá" ya se encuentra registrado en el sistema
	Cuando hago clic en crear 
	Entonces debería ser capaz de ver un mensaje "Cliente ya registrado, por favor introduce información nueva"

Scenario: Agregar un cliente sin éxito
	Dado que el cliente "Vanessa Alcalá" no se encuentra registrado en el sistema 
	Cuando hago clic en crear
	Entonces debería ser capaz de ver un mensaje con "Información insuficiente, por favor llene todos los campos"