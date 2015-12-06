Feature: Modificar Proveedores
    Con el fin de poder actualizar la informacion de un proveedor
    Como empleado registrado
    Quiero modificar los proveedores existentes

Scenario: Modificar proveedor
	Given Que el proveedor "postres fríos" se encuentra registrado AND me encuentro en la pantalla de editar
	When Cambio el nombre por "Cafe Americano" AND hago clic en el boton de modificar
	Then Puedo ver en la lista de proveedores registrados al proveedor "Cafe Americano"