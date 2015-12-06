Feature: Ver Promociones
    Con el fin de poder realizar una compra
    Como cliente del café cacahuate soft
    Visualizaré las promociones del día para hacer una mejor elección

Scenario: Mostrar promociones del día
    Given Que hoy es día de promociones
    When Oprimo el botón de ver promociones
    Then Puedo ver una lista con los productos que tienen promocion