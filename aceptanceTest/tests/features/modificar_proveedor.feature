Feature: Modificar Proveedores
    Con el fin de poder actualizar la informacion de un proveedor
    Como empleado registrado
    Quiero modificar los proveedores existentes

Scenario: Modificar proveedor
	Given Que el proveedor "cafe" se encuentra registrado
	When Cambio el nombre por "Cafe Americano" AND hago clic en el boton de modificar
	Then Puedo ver el mensaje "Proveedor modificado exitosamente"

Scenario: Modificar proveedor sin exito
	Given Que el proveedor "cafe" se encuentra registrado
	When Cambio el nombre por "" AND hago clic en el boton de modificar
	Then Puedo ver el mensaje "El proveedor no ha sido modificado exitosamente"