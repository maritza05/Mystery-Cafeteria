Feature: Como usuario de la cafeteria
         quiero visualizar las ventas realizadas a proveedores de un día
         en especifico

Scenario: Visualizar ventas del 12/06/09
    Given Que selecciono el día "2009-06-12" en la caja de texto
    When Oprimo el botón de buscar
    Then Puedo ver "Estas son las Ventas del "2009-06-12" en la cabecera
de la lista de ventas

Scenario: Visualizar ventas del 04/12/15
    Given Que selecciono el día "2015-12-15" en la caja de texto
    When Oprimo el botón de buscar
    Then Puedo ver "Estas son las Ventas del "2015-12-15" en la cabecera
de la lista de ventas