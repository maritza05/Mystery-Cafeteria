Feature: Cancelar compra
    Con el fin de poder reconsiderar mi eleccion
    Como cliente del café cacahuate soft
    cancelaré una compra

Scenario: Cancelar una compra
	Given la compra "001" esta en proceso
	When Oprimo el botón de cancelar 
	Then Puedo ver el mensaje "Compra cancelada"