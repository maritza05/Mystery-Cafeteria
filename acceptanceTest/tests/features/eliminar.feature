Feature: Eliminar empleado
	Con el fin de tener control de los empleados actuales
	Como administrador 
	Quiero eliminar un empleado.

Scenario: Eliminar empleado existente 
	Dado que el empleado "Manuel" se encuentra registrado en el sistema
	Cuando hago clic en el boton eliminar empleado
	Entonces debo ser capaz de ver la lista con los empleados