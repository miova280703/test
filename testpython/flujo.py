from selenium import webdriver

#para importaciones dentro del paquete de selenium
###By para el filtrado de elementos
from selenium.webdriver.common.by import By
#WebDriverWait para la espera de aparicion de elementos, util cuando se manejan animaciones
###importante usar el poll_frecuency en 1 segundo
from selenium.webdriver.support.wait import WebDriverWait

#Keys para el envio de acciones de teclado cuando ciertos elementos no son alcanzables por su dinamismo
from selenium.webdriver.common.keys import Keys
import time

class TestFlujoCompleto:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def goRoot(self):
        self.driver.get("https://demoqa.com/")

    def runFormulario(self):
        self.goRoot()

# flujo 1
        tarjetas_inicio = self.driver.find_elements(By.CLASS_NAME, "card.mt-4.top-card")
        for tarjeta in tarjetas_inicio:
            if tarjeta.text == "Elements":
                tarjeta.click()
                break

        itemscb = self.driver.find_elements(By.ID, "item-1")
        for item in itemscb:
            if item.text == "Check Box":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                item.click()
                break

        boton_expandir = self.driver.find_element(By.CLASS_NAME, "rct-option.rct-option-expand-all")
        boton_expandir.click()

        checkboxs = self.driver.find_elements(By.CLASS_NAME,"rct-title")
        for checkbox in checkboxs:
            if checkbox.text == "Word File.doc":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", checkbox)
                checkbox.click()
                # break
            if checkbox.text == "Excel File.doc":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", checkbox)
                checkbox.click()
                break
        time.sleep(2)

# flujo 2
        itemsdp = self.driver.find_elements(By.ID, "item-8")
        for item in itemsdp:
            if item.text == "Dynamic Properties":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                item.click()
                break

        espera_boton = WebDriverWait(self.driver, 5, poll_frequency=1).until(lambda d: d.find_element(By.ID, "enableAfter"))
        espera_boton.click()
        time.sleep(2)

# flujo 3
        itemswt = self.driver.find_elements(By.ID, "item-3")
        for item in itemswt:
            if item.text == "Web Tables":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                item.click()
                break

        borrar_boton = self.driver.find_element(By.ID, "delete-record-1")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", borrar_boton)
        borrar_boton.click()

        agregar_boton = self.driver.find_element(By.ID, "addNewRecordButton")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", agregar_boton)
        agregar_boton.click()

        open_modal = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.ID,"registration-form-modal"))
        time.sleep(2)
        assert open_modal.text == 'Registration Form' #da error, no sé por qué

        input_firstname = self.driver.find_element(By.ID, "firstName")
        input_firstname.send_keys("Iovana")
        input_lastname = self.driver.find_element(By.ID, "lastName")
        input_lastname.send_keys("Miranda")
        input_email = self.driver.find_element(By.ID, "userEmail")
        input_email.send_keys("cmiranda@bi.com.gt")
        input_age = self.driver.find_element(By.ID, "age")
        input_age.send_keys("25")
        input_salary = self.driver.find_element(By.ID, "salary")
        input_salary.send_keys("8000")
        input_department = self.driver.find_element(By.ID, "department")
        input_department.send_keys("Guatemala")

        enviar_boton = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", enviar_boton)
        enviar_boton.click()
        time.sleep(2)
        # verificacion = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.CLASS_NAME,"col-12.mt-4.col-md-6"))

# flujo 4
        elementos = self.driver.find_elements(By.CLASS_NAME, "header-wrapper")
        for elemento in elementos:
            if elemento.text == "Elements\n ":
                # self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                elemento.click()
            if elemento.text == "Forms\n ":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                elemento.click()
                break

        
        time.sleep(3)
        elemetosforms = self.driver.find_elements(By.ID, "item-0")
        for elementoform in elemetosforms:
            if elementoform.text == 'Practice Form':
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elementoform)
                elementoform.click()
                break

        input_firstname4 = self.driver.find_element(By.ID, "firstName")
        input_firstname4.send_keys("Claudia Iovana")

        input_lastname4 = self.driver.find_element(By.ID, "lastName")
        input_lastname4.send_keys("Miranda Alvarez")

        input_email4 = self.driver.find_element(By.ID, "userEmail")
        input_email4.send_keys("cmiranda@bi.com.gt")

        genders = self.driver.find_elements(By.CLASS_NAME,"custom-control-label")
        for gender in genders:
            if gender.text == "Female":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", gender)
                gender.click()
                break

        input_movil4 = self.driver.find_element(By.ID, "userNumber")
        input_movil4.send_keys("1234567890")

        input_birthday4 = self.driver.find_element(By.ID, "dateOfBirthInput")
        input_birthday4.click()
        input_month4 = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        input_month4.click()
        month4 = input_month4.find_element(By.CSS_SELECTOR, "option[value='6']")
        month4.click()
        input_year4 = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        input_year4.click()
        year4 = input_year4.find_element(By.CSS_SELECTOR, "option[value='1998']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", year4)
        year4.click()
        input_day = WebDriverWait(self.driver, timeout=10, poll_frequency=2).until(lambda d: d.find_element(By.CSS_SELECTOR, "div[class='react-datepicker__day react-datepicker__day--028']"))
        self.driver.execute_script("arguments[0].scrollIntoView(true)", input_day)
        input_day.click()

        input_subject4 = self.driver.find_element(By.ID, "subjectsInput")
        input_subject4.send_keys("Maths")
        input_subject4.send_keys(Keys.ENTER)

        input_hobbie4 = self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
        input_hobbie4.click()

        filePath = "/home/iova/prueba.txt";
        input_picture4 = self.driver.find_element(By.ID, "uploadPicture")
        input_picture4.send_keys(filePath)

        input_address4 = self.driver.find_element(By.ID, "currentAddress")
        input_address4.send_keys("Banco Industrial Zona 4 Torre 1")

        input_state4 = self.driver.find_element(By.ID, "react-select-3-input")
        input_state4.send_keys("NCR")
        input_state4.send_keys(Keys.ENTER)

        input_city4 = self.driver.find_element(By.ID, "react-select-4-input")
        input_city4.send_keys("Delhi")
        input_city4.send_keys(Keys.ENTER)

        button_submit4 = self.driver.find_element(By.ID, "submit")
        button_submit4.send_keys(Keys.ENTER)

        verificacion = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.ID,"example-modal-sizes-title-lg"))
        time.sleep(2)
        assert verificacion.text == 'Thanks for submitting the form' 

        button_close4 = self.driver.find_element(By.ID, "closeLargeModal")
        button_close4.send_keys(Keys.ENTER)
        time.sleep(2)

# flujo 5
        for elemento in elementos:
            if elemento.text == "Forms\n ":
                # self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                elemento.click()
            if elemento.text == "Book Store Application\n ":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                elemento.click()
                break

        
        time.sleep(3)
        elemetosbooks = self.driver.find_elements(By.ID, "item-2")
        for elementobook in elemetosbooks:
            if elementobook.text == 'Book Store':
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elementobook)
                elementobook.click()
                break
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0)")
        input_search5 = self.driver.find_element(By.ID, "searchBox")
        input_search5.click()
        input_search5.send_keys("Understanding ECMAScript 6")

        clic_serch5 = self.driver.find_element(By.LINK_TEXT, "Understanding ECMAScript 6")
        clic_serch5.click()
        time.sleep(5)

        clic_web5 = self.driver.find_elements(By.CSS_SELECTOR, "label[class='form-label']")
        paginaactual = self.driver.current_window_handle
        nuevapagina = self.driver.current_window_handle
        for clic in clic_web5:
            if clic.text == "https://leanpub.com/understandinges6/read":
                self.driver.execute_script("arguments[0].scrollIntoView(true)", clic)
                clic.click()
                break
        nuevapagina = self.driver.window_handles[1]
        self.driver.switch_to.window(nuevapagina)
        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(paginaactual)
        time.sleep(2)

        button_back5 = self.driver.find_element(By.ID, "addNewRecordButton")
        button_back5.send_keys(Keys.ENTER)
        


a = TestFlujoCompleto()

a.runFormulario()

input("Presione para continuar")