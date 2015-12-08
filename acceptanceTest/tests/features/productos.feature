Feature: Como administrador de la cafeteria
    quiero añadir un producto nuevo
    para actualizar inventario en el inventario

    Scenario: Dado que llego producto nuevo
          Quiero Añadir producto ingresando "nombre", "descripcion" y "precio"
          Cuando envio el formulario 
          Entonces la lista de productos se mostrara actualizada con producto añadido

    Scenario: Dado que quiero añadir producto con campos vacios
          Quiero Añadir producto ingresando "nombre", "descripcion" y "precio"
          Cuando envio formulario detecta campos vacios
          Entonces regresara error de campo vacio

    Scenario: Dado que quiero añadir producto ya existente
          Quiero Añadir producto ingresando "nombre", "descripcion" y "precio"
          Cuando envio formulario detecta nombre repetido
          Entonces regresa pagina "Productos"