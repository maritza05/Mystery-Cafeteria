Feature: Mostrar menú de día de la semana
    Con el fin de poder elegir algo de comer
    Como cliente del café cacahuate soft
    Visualizaré el menú del día

Scenario: Mostrar el menu del día de la semana
	Given Que hoy es "lunes"
	When Oprimo el botón de menu 
	Then Puedo ver el mensaje "Menu lunes"