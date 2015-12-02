Feature: Cancelar compra
    Con el fin de poder reconsiderar mi eleccion
    Como cliente del café cacahuate soft
    cancelaré una compra

Scenario: Cancelar un compra
    Dado que realice la compra "001"
    Cuando solicito "cancelar compra" y acepto cancelar la compra
    Entonces el resultado debe ser "Compra cancelada"