Feauture: Como administrador de la cafeteria
   quiero consultar el inventario
   para tener el control del stock de productos

   Scenario: Cuando quiero Acceder al inventario de productos
      Dado que quiero conocer el "/inventario"
      Entonces veo la pagina de "Inventario"

   Scenario: Cuando quiero añador cantidad de producto
      Dado que quiero añadir "cantidad" a "productos"
      Entonces veo la pagina de "Añadir Inventario"

   Scenario: Cuando quiero restar cantidad del producto vendido
      Dado que quiero restar "cantidad" al "producto" 
      Entonces veo la pagina de "Restar Inventario" 