Feature: Ver Promociones
    Con el fin de poder realizar una compra
    Como cliente del café cacahuate soft
    Visualizaré las promociones del día para hacer una mejor elección

Scenario: Mostrar promociones del día
    Dado que hoy es "Lunes"
    Cuando solicito "Realizar compra"
    Entonces la pantalla mostrará "Esta es la promoción del lunes: Café 2 x 1" 