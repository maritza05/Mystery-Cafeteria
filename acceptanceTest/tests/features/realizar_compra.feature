Feature: Realizar compras
    Con el fin de consumir en la cafeteria
    Como cliente registrado
    Quiero hacer compras

Scenario: Compra de productos
    Dado que tengo los productos "café" y "pastel" existentes en almacén
    Cuando doy click en "realizar compra"
    Entonces debería ser capaz de ver el mensaje "Compra realizada con éxito"

Scenario: Compra fallida de  producto
    Dado que el producto "galleta" se ha agotado
    Cuando doy click en "realizar compra"
    Entonces el resultado debe de ser "producto insuficiente en el almacen"