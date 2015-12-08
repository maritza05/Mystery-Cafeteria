Feature: Modificar puestos
	Con el fin de poder actualizar la información de un puesto
	Como administrador
	Quiero modificar los puestos

Scenario: Modificar puestos exitosamente
	Dado que el puesto "repartidor" se encuentra registrado AND me encuentro en la pantalla de editar
	Cuando cambio el nombre por "repartidor en moto" AND hago clic en el boton de modificar
	Entonces puedo ver en la lista actualizada de puestos con el puesto "repartidor en moto"
