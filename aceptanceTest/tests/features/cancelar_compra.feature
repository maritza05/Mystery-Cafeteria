Feature: Cancelar compra
    Con el fin de poder reconsiderar mi eleccion
    Como cliente del café cacahuate soft
    Cancelaré una compra

Scenario: Cancelar una compra antes de pagar
	Given Que la compra "001" esta en proceso
	When Oprimo el botón de cancelar compra 
	Then Puedo ver una lista con las compras que he realizado