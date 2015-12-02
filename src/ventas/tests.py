from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


# Create your tests here.
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_register_sell(self):
        # The employee goes to the homepage
        self.brower.get('http://localhost:8000')

        # He notices the page title and header mention Compras
        self.assertIn('Compras', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Compras a Proveedores', header_text)

        # He is invited to select the provider
        selection_provider = self.browser.find_element_by_id('id_proveedor')
        self.assertEqual(selection_provider.get_attribute('value'),
                'Coffe Alegre'
                )

        # He selectes "Coffee Provider" 
        selection_provider.send_keys(Keys.ENTER)

        # He is invited to type his ID into a text box
        inputbox_employee = self.browser.find_element_by_id('id_empleado')
        self.assertEqual(inputbox_employee.get_attribute('placeholder'),
                'Ingrese su ID de empleado'
                )

        # He types "EMP01" into a text box
        inputbox.send_keys('EMP01')

        # He is invited to select the inventario
        inputbox_inventario = self.browser.find_element_by_id('id_inventario')
        self.assertEqual(inputbox_inventario.get_attribute('placeholder'),
                'Ingrese el ID del inventario'
                )

        # He types "INV01" into a text box
        inputbox_inventario.send_keys('INV01')

        # He is invited to select the actual date
        date_field = self.browser.find_element_by_id('id_datechooser')
        self.assertEqual(date_field.get_attribute('date'),
                'Seleccione la fecha de la compra'
                )

        # He types "01/12/2015" into a date field
        date_field.send_keys('01/12/2015')

        # He is invited to add a amount
        inputbox_amount = self.browser.find_element_by_id('id_amount')
        self.assertEqual(inputbox_amount.get_attribute('placeholder')
                'Ingrese el monto de la compra'
                )
        # He types "650.50" into a a text box
        inputbox_amount.send_keys('650.50')

        # He sees the button "Registrar Compra"
        button_save = self.browser.find_element_by_id('id_buttonSave')
        self.assertEqual(button_save.get_attribute('text')
                'Registrar Compra'
                )
        # He selects the button
        button_save.click()

        # The page updates and now the page shows the message "Compra registrada de manera exitosa"
        header_successful = self.browser.find_element_by_tag('h1').text
        self.assertEqual(header_sucessful, 'Compra registrada de manera exitosa')

        self.fail('Finish the test!')

