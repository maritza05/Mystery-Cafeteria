Feature: Eliminar proveedores
    Con el fin de tener control de los proveedores actuales
    Como empleado registrado
    Quiero eliminar proveedores

Scenario: Eliminar proveedor
	Given El proveedor "Café capuccino" se encuentra registrado
	When Oprimo el botón de elminar 
	Then Puedo ver el mensaje "Proveedor eliminado exitosamente"

Scenario: Eliminar proveedor
	Given El proveedor "Café capuccino" se encuentra registrado
	When Oprimo el botón de elminar 
	Then Ya no puedo ver el proveedor "Café capuccino" en la lista de proveedores