Feature: Mostrar menú de día de la semana
    Con el fin de poder elegir algo de comer
    Como cliente del café cacahuate soft
    Visualizaré el menú del día

Scenario: Mostrar el menú del día de la semana
    Dado que hoy es "Lunes"
    Cuando solicito "visualizar menú del día"
    Entonces podre visualizar "Menú lunes: capuchino vainilla, cupcake" 