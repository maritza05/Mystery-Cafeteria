Feature: Agregar empleados nuevos
	Con el fin de poder ingresar nuevos empleados 
	Como un administrador
	Quiero agregar nuevos empleados.

Scenario: Agregar empleado exitosamente
	Dado que me encuentro en la pagina principal como administrador
	Cuando hago clic en el boton nuevo empleado
	Entonces debo ser capaz de ver un mensaje "empleado agregado"

