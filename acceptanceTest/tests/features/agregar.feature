Feature: Agregar puestos nuevos
	Con el fin de poder ingresar nuevos puestos	Como un administrador
	Quiero agregar nuevos puestos.

Scenario: Agregar puesto exitosamente
	Dado que me encuentro en la pagina principal como administrador
	Cuando hago clic en el boton nuevo puesto
	Entonces debo ser capaz de ver un mensaje "puesto agregado"

