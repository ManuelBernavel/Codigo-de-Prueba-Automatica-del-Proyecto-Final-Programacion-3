# Librerías
import random
import string
import HtmlTestRunner
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Pruebas_historias(unittest.TestCase):

    def setUp(self):
        # Generar credenciales automatico para la automatizacion
        length_of_string = 8
        self.stringExample = ''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(length_of_string))
        self.driver = webdriver.Chrome(
            'C:\\Users\\FidelGeronimoGarcia\\Downloads\\chromedriver.exe')
# ******************** TESTING DEL LOGIN ****************

    def test_login_Existe_pagina(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_Existe_pagina.png')
        time.sleep(2)

    def test_login_input_nombre(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuario"]')
        usuario.click()

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_input_nombre.png')
        time.sleep(2)

    def test_login_input_pass(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        password = self.driver.find_element(
            By.XPATH, '//*[@id="pass"]')
        password.click()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_input_pass.png')
        time.sleep(2)

    def test_login_input_button(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        a = ActionChains(self.driver)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="submit"]')
        a.move_to_element(button).perform()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_input_button.png')
        time.sleep(2)

    def test_login_fallido_sin_usuarios(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuario"]')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="pass"]')
        time.sleep(2)
        usuario.send_keys("Emaik@testing@.com")
        password.send_keys('passwordTest')
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertIn('Login', self.driver.title)
        # confirmacion de cuadro de error
        errorMessage = self.driver.find_element(
            By.XPATH, '//*[@id="mensajes"]/p').get_attribute('class')
        self.assertIn('error', errorMessage)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_fallido_sin_usuarios.png')
        time.sleep(2)

    def test_login_fallido_campos_vacios(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuario"]')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="pass"]')
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        # self.assertIn('Login', self.driver.title)

        # confirmacion de cuadro de error
        errorMessage = self.driver.find_element(
            By.XPATH, '//*[@id="mensajes"]/p').get_attribute('class')
        self.assertIn('error', errorMessage)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_login_fallido_sin_usuarios.png')
        time.sleep(2)

    def test_login_exitoso(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/index.html')
        self.assertIn('Login', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source
        # Yendo a registrar usuarios
        time.sleep(3)
        usuario = self.driver.find_element(
            By.XPATH, '/html/body/form/a')
        usuario.click()
        time.sleep(2)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuarioRegistro"]')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="passRegistro"]')
        time.sleep(2)
        usuario.send_keys("fidel")
        password.send_keys('fidel')
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertIn('Login', self.driver.title)

        # busqueda de campos en la pagina web
        time.sleep(3)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuario"]')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="pass"]')
        time.sleep(2)
        usuario.send_keys("fidel")
        password.send_keys('fidel')
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertIn('Task App', self.driver.title)

        # Captura de pantalla
        self.driver.save_screenshot('capturas/test_login_exitoso.png')
        time.sleep(2)
# ******************** TESTING DEL REGISTRO ****************

    def test_Registro_exitoso(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # Yendo a registrar usuarios
        time.sleep(2)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuarioRegistro"]')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="passRegistro"]')
        time.sleep(2)
        usuario.send_keys("fidel")
        password.send_keys('fidel')
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertIn('Login', self.driver.title)

        # Captura de pantalla
        time.sleep(3)
        self.driver.save_screenshot('capturas/test_Registro_exitoso.png')

    def test_registro_Existe_pagina(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_registro_Existe_pagina.png')
        time.sleep(2)

    def test_registro_input_nombre(self):
        # Busqueda de la pagina
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(2)
        usuario = self.driver.find_element(
            By.XPATH, '//*[@id="usuarioRegistro"]')
        time.sleep(1)
        usuario.click()

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_registro_input_nombre.png')
        time.sleep(2)

    def test_registro_input_pass(self):
        # Busqueda de la pagina
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        password = self.driver.find_element(
            By.XPATH, '//*[@id="passRegistro"]')
        password.click()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_registro_input_pass.png')
        time.sleep(2)

    def test_registro_input_button(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        a = ActionChains(self.driver)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="submit"]')
        a.move_to_element(button).perform()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_registro_input_button.png')
        time.sleep(2)

    def test_registro_fallido_campos_vacios(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/registro/registro.html')
        self.assertIn('Registro', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="submit"]')
        button.click()
        time.sleep(2)

        # confirmacion de cuadro de error
        errorMessage = self.driver.find_element(
            By.XPATH, '//*[@id="mensajes"]/p').get_attribute('class')
        self.assertIn('error', errorMessage)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_registro_fallido_campos_vacios.png')
        time.sleep(2)
# ******************** TESTING DE PAGINA DE TAREAS ****************

    def test_existe_pagina_tareas(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_existe_pagina_tareas.png')
        time.sleep(2)

    def test_existe_input_titulo_tarea(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        tareaTitulo = self.driver.find_element(
            By.XPATH, '//*[@id="title"]')
        time.sleep(1)
        tareaTitulo.click()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_existe_input_titulo_tarea.png')
        time.sleep(2)

    def test_existe_input_descripcion_tarea(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        tareaDescripcion = self.driver.find_element(
            By.XPATH, '//*[@id="description"]')
        time.sleep(1)
        tareaDescripcion.click()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_existe_input_descripcion_tarea.png')
        time.sleep(2)

    def test_existe_boton_guardar_tarea(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        time.sleep(3)
        a = ActionChains(self.driver)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="formTask"]/button')
        a.move_to_element(button).perform()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_existe_boton_guardar_tarea.png')
        time.sleep(2)

    def test_creacion_tarea(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        titulo = self.driver.find_element(
            By.XPATH, '//*[@id="title"]')
        descripcion = self.driver.find_element(
            By.XPATH, '//*[@id="description"]')
        titulo.send_keys("Titulo de prueba")
        descripcion.send_keys('Descripcion de prueba')
        time.sleep(1)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="formTask"]/button')
        button.click()
        time.sleep(1)
        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_creacion_tarea.png')
        time.sleep(1)

    def test_existe_task_tarea_creada(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        titulo = self.driver.find_element(
            By.XPATH, '//*[@id="title"]')
        descripcion = self.driver.find_element(
            By.XPATH, '//*[@id="description"]')
        titulo.send_keys("Titulo de prueba")
        descripcion.send_keys('Descripcion de prueba')
        time.sleep(1)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="formTask"]/button')
        button.click()
        time.sleep(1)

        # busqueda de campos en la pagina web
        tarea = self.driver.find_element(
            By.XPATH, '//*[@id="tasks"]/div/div')

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_existe_task_tarea_creada.png')
        time.sleep(1)

    def test_borrar_tarea(self):
        # Busqueda de la pagina
        self.driver = self.driver
        self.driver.get(
            'https://fanciful-haupia-a13a45.netlify.app/taskproject/index.html')
        self.assertIn('Task App', self.driver.title)
        assert "No se encontro el elemento:" not in self.driver.page_source

        # busqueda de campos en la pagina web
        titulo = self.driver.find_element(
            By.XPATH, '//*[@id="title"]')
        descripcion = self.driver.find_element(
            By.XPATH, '//*[@id="description"]')
        titulo.send_keys("Titulo de prueba")
        descripcion.send_keys('Descripcion de prueba')
        time.sleep(1)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="formTask"]/button')
        button.click()
        time.sleep(1)

        # busqueda de campos en la pagina web
        borrar = self.driver.find_element(
            By.XPATH, '//*[@id="tasks"]/div/div/p/a')
        borrar.click()
        time.sleep(1)

        # captura de pantalla
        self.driver.save_screenshot(
            'capturas/test_borrar_tarea.png')
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reporte'))
