from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


# Create your tests here.
class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_register_employee(self):
       #empleado accede a la página
        self.brower.get('http://localhost:8000')

        # El encabezado de la página dice Registro
        self.assertIn('Registro', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Registro Empleados', header_text)

        # Se realiza el registro del empleado
        nombre_empleado = self.browser.find_element_by_id('employee_name')
        self.assertEqual(nombre_empleado.get_attribute('placeholder'),
                'Ingrese el nombre del empleado'
                )
        nombre_empleado.send_keys('Manuel')


        password_empleado = self.browser.find_element_by_id('password_employee')
        self.assertEqual(password_empleado.get_attribute('placeholder'),
                'Ingrese la contraseña del empleado'
                )
        password_cliente.send_keys('employeeMA1234')

        apellido_paterno = self.browser.find_element_by_id('apellido_paterno')
        self.assertEqual(apellido_paterno.get_attribute('placeholder'),
                'Ingrese el apellido paterno del empleado'
                )
        apellido_paterno.send_keys('Almaraz')

        apellido_materno = self.browser.find_element_by_id('apellido_materno')
        self.assertEqual(apellido_materno.get_attribute('placeholder'),
                'Ingrese el apellido materno del empleado'
                )
         apellido_materno.send_keys('Torres')

        email = self.browser.find_element_by_id('email')
        self.assertEqual(email.get_attribute('placeholder'),
                'Ingrese el email del empleado'
                )
         email.send_keys('manuel_12@gmail.com')

        nombre_usuario = self.find_element_by_id('user_name')
        self.assertEqual(nombre_usuario.get_attribute('placeholder'),
                'Ingrese el nombre de usuario del empleado'
                )
        nombre_usuario.send_keys('Manuelin')

        puesto_empleado = self.browser.find_element_by_id('id_puesto')
        self.assertEqual(puesto_empleado.get_attribute('value'),
                'Cajero'
                )
        puesto_empleado.send_keys(Keys.ENTER)


        boton_registrar = self.driver.find_element_by_id('registrer_button_employee')
        self.assertEqual(boton_registrar.get_attribute('text'),
                'Registrar'
        boton_registrar.click()

         # Página actualizada con el encabezado "Empleado registrado exitosamente"
        header_successful = self.browser.find_element_by_tag('h1').text
        self.assertEqual(header_sucessful, 'Empleado registrado exitosamente')

        self.fail('Finish the test!')
