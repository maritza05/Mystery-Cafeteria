Feature: Eliminar proveedores
    Con el fin de tener control de los proveedores actuales
    Como empleado registrado
    Quiero eliminar proveedores

Scenario: Eliminar proveedor
	Given El proveedor "Café capuccino" se encuentra registrado en el sistema
	When Oprimo el botón de elminar proveedor "3"
	Then Puedo ver una lista con los proveedores registrados