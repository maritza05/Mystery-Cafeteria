Feature: Ver lista de Proveedores
    Con el fin de informarme sobre los proveedores de la sucursal
    Como empleado registrado
    Quiero consultar los proveedores existentes

Scenario: Consulta de proveedores
    Given Que he ingresado al sistema como "Maritza"
    When Oprimo el botón de proveedores
    Then Puedo ver el mensaje "Proveedores de la cafeteria"

Scenario: Consulta de proveedores
    Given Que he ingresado al sistema como "Maritza"
    When Oprimo el botón de ver proveedor
    Then Puedo ver el mensaje "Proveedor: "