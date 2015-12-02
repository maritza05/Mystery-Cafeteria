Feature: Ver empleados registrados
Con el fin de ver los empleados afiliados a la sucursal
Como administrador
Quiero cosultar los empleados.

Scenario: Consulto empleado con ID exitosamente 
	Dado que el empleado "Manuel Almaraz" se encuentra registrado en el sistema
	Cuando hago clic en el boton consultar
	Entonces debo ser capaz de ver el mensaje "EM-001: Manuel Almaraz"

Scenario: Consulto empleado sin ID válido
	Dado que el empleado "Manuel Almaraz" no se encuentra registrado en el sistema con el ID "EM-001"
	Cuando realizo la consulta del ID "EM-001"
	Entonces debería se capaz de ver "No existe con empleado asociado con este ID"

Scenario: Consulto todos los empleados registrados exitosamente
	Dado que existen cuatro empleados registrados en el sistema 
	Cuando solicito "Consultar todos los empleados"
	Entonces debería ser capaz de ver "[EM-001, EM-002, EM-003, EM-004]"

Scenario: No existen empleados registrados
	Dado que no existe ningún empleados registrado
	Cuando solicito "Consultar todos los clientes"
	Entonces debería ser capaz de ver "Ningún empleados
    registrado en el sistema."
