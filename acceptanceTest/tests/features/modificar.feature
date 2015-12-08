Feature: Modificar Empleado
	Con el fin de poder actualizar la información de un empleado
	Como administrador
	Quiero modificar los empleados

Scenario: Modificar empleados exitosamente
	Dado que el empleado "Manuel" se encuentra registrado AND me encuentro en la pantalla de editar
	Cuando cambio el nombre por "Martin" AND hago clic en el boton de modificar
	Entonces puedo ver en la lista actualizada de empleados con el empleado "Martin"
