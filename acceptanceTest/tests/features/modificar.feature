Feature: Modificar Clientes
Con el fin de poder actualizar la información de un cliente
Como empleado registrado 
Quiero modificar los clientes

Scenario: Modificar clientes
	Dado que el cliente "Vanessa Alcalá" se encuentra registrado en el sistema
	Cuando hago clic en modificar
	Entonces debería ser capaz de ver "Vanessa Alcalá vane-06@gmail.com "

Scenario: Guardar datos exitosamente
	Dado que el cliente "Vanessa Alcalá" se encuentra registrado con el ID "CL-001"
	Cuando hago clic en guardar
	Entonces debería ser capaz de ver un mensaje con "El cliente ha sido modificado exitosamente"

Scenario: Modificar un cliente sin éxito
	Dado que el cliente "Vanessa Alcalá"  se encuentra registrado en el sistema 
	Cuando hago clic en guardar
	Entonces debería ser capaz de ver un mensaje con "Información insuficiente, por favor llene todos los campos"