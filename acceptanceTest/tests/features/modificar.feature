Feature: Modificar Empleado
Con el fin de poder actualizar la información de un empleado
Como administrador
Quiero modificar los empelados

Scenario: Modificar empleado
	Dado que el empleado "Manuel Almaraz" se encuentra registrado con el ID "EM-001"
	Cuando hago clic en modificar
	Entonces debo ser capaz de ver el mensaje "Manuel Almaraz manuel-06@gmail.com "

Scenario: Guardar datos exitosamente
	Dado que el empleado "Manuel Almaraz" se encuentra registrado con el ID "EM-001"
	Cuando hago clic en guardar
	Entonces debería ser capaz de ver un mensaje con "El empleado ha sido modificado exitosamente"

Scenario: Modificar un empleado sin éxito
	Dado que el empleado "Manuel Almaraz"  se encuentra registrado en el sistema 
	Cuando hago clic en guardar
	Entonces debería ser capaz de ver un mensaje con "Información insuficiente, por favor llene todos los campos"