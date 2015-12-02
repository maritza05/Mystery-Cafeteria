Feature: Realizar compras
    Con el fin de consumir en la cafeteria
    Como cliente registrado
    Quiero hacer compras

Scenario: Compra exitosa
    Given Que estoy realizando la compra "34"
    When Oprimo el botón de comprar
    Then Puedo ver la opcion de "nueva compra"

Scenario: Compra sin exito
    Given Que estoy realizando la compra "35"
    When Oprimo el botón de comprar
    Then Puedo ver el mensaje "lo sentimos, tu compra no pudo ser realizada"