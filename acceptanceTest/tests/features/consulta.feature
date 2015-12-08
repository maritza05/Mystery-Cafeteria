Feature: Ver empleados registrados
Con el fin de ver los empleados con los que cuenta la sucursal
Como un administrador registrado 
Quiero cosultar los empleados.

Scenario: Consulta de empleados registrados en el sistema
    Dado que he ingresado al sistema como administrador
    Cuando hago clic en el boton consultar
    Entonces debo ser capaz de ver el mensaje "Empleado"


