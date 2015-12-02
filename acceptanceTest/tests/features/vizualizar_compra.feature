Feature: Visualizar compra
    Con el fin de observar los gastos de lo consumido 
    Como cliente registrado
    visualizaré el total de la compra

Scenario: Visualizar total
    Dado que he ingresado al sistema como el cliente "Maritza"
    Cuando selecciono la opción de Ver Compras y selecciono una "compra"
    Entonces podré visualizar "total: XX.XX"