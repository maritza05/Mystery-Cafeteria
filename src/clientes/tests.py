from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


# Create your tests here.
class ClientTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_register_client(self):
       #Cliente accede a la página
        self.brower.get('http://localhost:8000')

        # El encabezado de la página dice Registro
        self.assertIn('Registro', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Registro Clientes', header_text)

        # El cliente se registra
        nombre_cliente = self.browser.find_element_by_id('client_name')
        self.assertEqual(nombre_cliente.get_attribute('placeholder'),
                'Ingrese su nombre'
                )
        nombre_cliente.send_keys('Vanessa')


        password_cliente = self.browser.find_element_by_id('password_client')
        self.assertEqual(password_cliente.get_attribute('placeholder'),
                'Ingrese su contraseña'
                )
        password_cliente.send_keys('cafe1234')

        apellido_paterno = self.browser.find_element_by_id('apellido_paterno')
        self.assertEqual(apellido_paterno.get_attribute('placeholder'),
                'Ingrese su apellido paterno'
                )
        apellido_paterno.send_keys('Alcalá')

        apellido_materno = self.browser.find_element_by_id('apellido_materno')
        self.assertEqual(apellido_materno.get_attribute('placeholder'),
                'Ingrese su apellido materno'
                )
         apellido_materno.send_keys('Ramírez')

        email = self.browser.find_element_by_id('email')
        self.assertEqual(email.get_attribute('placeholder'),
                'Ingrese su email'
                )
         email.send_keys('vane_19940605@hotmail.com')

        nombre_usuario = self.find_element_by_id('user_name')
        self.assertEqual(nombre_usuario.get_attribute('placeholder'),
                'Ingrese su nombre de usuario'
                )
        nombre_usuario.send_keys('VaneAR')


        boton_registrar = self.driver.find_element_by_id('registrer_button')
       self.assertEqual(boton_registrar.get_attribute('text'),
                'Registrar'
        boton_registrar.click()

         # Página actualizada con el encabezado "Cliente registrado exitosamente"
        header_successful = self.browser.find_element_by_tag('h1').text
        self.assertEqual(header_sucessful, 'Cliente registrado exitosamente')

        self.fail('Finish the test!')
