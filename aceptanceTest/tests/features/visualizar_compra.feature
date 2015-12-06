Feature: Visualizar compra
    Con el fin de observar los gastos de lo consumido 
    Como cliente registrado
    visualizaré el total de la compra

Scenario: Visualizar historial
    Given Que he ingresado al sistema como "Maritza"
    When Oprimo el botón de historial de compras
    Then Puedo ver "Compras realizadas hasta la fecha" por "Maritza"