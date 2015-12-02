Feature: Eliminar empleado
Con el fin de tener control de los empleados actuales
Como administrador 
Quiero eliminar un empleado.

Scenario: Eliminar empleado existente 
	Dado que el empleado "Manuel Almaraz" se encuentra registrado en el sistema
	Cuando hago clic en el botón eliminar
	Entonces debo ser capaz de ver el mensaje "Empleado eliminado Exitosamente"

Scenario: Eliminar un empleado no existenete
	Dado que el empleado "Manuel Almaraz" no se encuentra registrado.
	Cuando hago clic en eliminar
	Entonces debería ser capaz de ver un mensaje con "El empleado no existe".