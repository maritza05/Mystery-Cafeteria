Feature: Ver Promociones
    Con el fin de poder realizar una compra
    Como cliente del café cacahuate soft
    Visualizaré las promociones del día para hacer una mejor elección

Scenario: Mostrar promociones del día
    Given Que hoy es "Lunes"
    When Oprimo el botón de promociones
    Then Puedo ver el mensaje "Promocion: Cafe 2x1"

Scenario: Mostrar dia sin promociones
	Given Que hoy es "Domingo"
	When Oprimo el botón de promociones 
	Then Puedo ver el mensaje "Hoy no hay promociones"