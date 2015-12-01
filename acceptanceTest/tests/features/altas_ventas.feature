Feature: Como empleado de la cafeteria
        quiero registrar una venta
        para poder tener un control de las ventas realizadas a los proveedores

Scenario: Registrar la venta de un capuccino
    Given Que se compro al proveedor "1" producto con el nombre de "capuccino" 
    When Oprimo el botón de Registrar Venta
    Then Puedo ver el producto "capuccino" en la lista de productos del inventario


Scenario: Registrar la venta de 20 galletas
    Given Que se compro al proveedor "20" productos con el nombre de "galleta de chocolate" 
    When Oprimo el botón de Registrar Venta
    Then Puedo ver "20" productos con el nombre "galleta de chocolate" en la lista de productos del inventario