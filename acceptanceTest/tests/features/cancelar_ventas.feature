Feature: Como empleado de la cafeteria
        quiero cancelar las compras
        realizadas a los proveedores

Scenario: Cancelar la compra de 30 galletas
    Given Que selecciono la venta con el nombre de producto "galletas"
    When Oprimo el botón cancelar
    Then Puedo ver el mensaje "Venta cancelada"
    
Scenario: Cancelar la compra de 1 capuccino
    Given Que selecciono la venta con el nombre de producto "capuccino"
    When Oprimo el botón cancelar
    Then Puedo ver el mensaje "Venta cancelada"