Feature: Agregar empleados nuevos
Con el fin de poder tener más empleados
Como un administrador
Quierp agregar nuevos empleados.

Scenario: Agregar empleados exitosamente
	Dado que el empleado "Manuel Almaraz" no se encuentra registrado
	Cuando hago clic en crear
	Entonces debo ser capaz de ver un mensaje "EM-001:Manuel Almaraz agregado exitosamente"

Scenario: Agegar un empleado ya existente 
	Dado que el empleado "Manuel Almaraz" ya se encuentra registrado en el sistema
	Cuando hago clic en crear 
	Entonces debería ser capaz de ver un mensaje "Empleado ya registrado, por favor introduce información nueva"

Scenario: Agregar un empleado sin éxito
	Dado que el cliente Manuel Almaraz no se encuentra registrado en el sistema 
	Cuando hago clic en crear
	Entonces debería ser capaz de ver un mensaje con "Información insuficiente, por favor llene todos los campos"