Feature: Ver clientes registrados
Con el fin de ver los clientes afiliados a la sucursal
Como un empleado registrado 
Quiero cosultar los clientes.

Scenario: Consulto cliente con ID exitosamente 
	Dado que el cliente "Vanessa Alcalá" se encuentra registrado en el sistema
	Cuando hago clic en el botón consulta
	Entonces debo ser capaz de ver el mensaje "CL-001: Vanessa Alcalá"

Scenario: Consulto cliente sin ID válido
	Dado que el cliennte "Vanessa Alcalá" no se encuentra registrado en el sistema con el ID "CL-001"
	Cuando realizo la consulta del ID "CL-001"
	Entonces debería se capaz de ver "No existe con cliente asociado con este ID"

Scenario: Consulto todos los clientes registrados exitosamente
	Dado que existen cuatro clientes registrados en el sistema 
	Cuando solicito "Consultar todos los clientes"
	Entonces debería ser capaz de ver "[CLI-001, CLI-002, CLI-003, CLI-004]"

Scenario: No existen clientes registrados
	Dado que no existe ningún cliente registrado
	Cuando solicito "Consultar todos los clientes"
	Entonces debería ser capaz de ver "Ningún cliente registrado en el sistema."
