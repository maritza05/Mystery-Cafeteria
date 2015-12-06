Feature: Ver lista de Proveedores
    Con el fin de informarme sobre los proveedores de la sucursal
    Como empleado registrado
    Quiero consultar los proveedores existentes

Scenario: Consulta de proveedores registrados en la cafetería
    Given Que he ingresado al sistema como "Maritza" y me encuentro en la pagina principal
    When Oprimo el botón de ver proveedores
    Then Puedo ver los proveedores registrados en una lista "Proveedores"