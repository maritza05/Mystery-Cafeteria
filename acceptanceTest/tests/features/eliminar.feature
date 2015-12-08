Feature: Eliminar puesto
	Con el fin de tener control de los puestos actuales
	Como administrador 
	Quiero eliminar un puesto.

Scenario: Eliminar puesto existente 
	Dado que el puesto "repartidor" se encuentra registrado en el sistema
	Cuando hago clic en el boton eliminar puesto
	Entonces debo ser capaz de ver la lista con los puestos