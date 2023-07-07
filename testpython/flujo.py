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
        # Se inicializa el driver
        self.driver = webdriver.Chrome()
        # Se maximiza la ventana del driver
        self.driver.maximize_window()

    def goRoot(self):
        # Se navega a la pagina de demoqa
        self.driver.get("https://demoqa.com/")

    def runFormulario(self):
        # Se navega a la pagina de demoqa
        self.goRoot()

# flujo 1
        # Se obtienen las cartas de la pagina
        tarjetas_inicio = self.driver.find_elements(By.CLASS_NAME, "card.mt-4.top-card")
        # Se recorre cada carta
        for tarjeta in tarjetas_inicio:
            # Se verifica si el texto de la carta es igual a "Elements"
            if tarjeta.text == "Elements":
                # Se hace clic hasta la carta
                tarjeta.click()
                break

        # Se obtienen los items del menu de la pagina
        itemscb = self.driver.find_elements(By.ID, "item-1")
        # Se recorre cada item
        for item in itemscb:
            # Se verifica si el texto del item es igual a "Check Box"
            if item.text == "Check Box":
                # Se hace scroll hasta el item
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                # Se hace clic hasta el item
                item.click()
                break

        # Se obtiene el boton expandir todo
        boton_expandir = self.driver.find_element(By.CLASS_NAME, "rct-option.rct-option-expand-all")
        # Se hace clic en el boton
        boton_expandir.click()

        # Se obtienen los checkboxs de la pagina
        checkboxs = self.driver.find_elements(By.CLASS_NAME,"rct-title")
        # Se recorre cada checkbox
        for checkbox in checkboxs:
            # Se verifica si el texto del checkbox es igual a "Word File.doc"
            if checkbox.text == "Word File.doc":
                # Se hace scroll hasta el checkbox
                self.driver.execute_script("arguments[0].scrollIntoView(true)", checkbox)
                # Se hace clic hasta el checkbox
                checkbox.click()
                # break
            # Se verifica si el texto del checkbox es igual a "Excel File.doc"
            if checkbox.text == "Excel File.doc":
                # Se hace scroll hasta el checkbox
                self.driver.execute_script("arguments[0].scrollIntoView(true)", checkbox)
                # Se hace clic hasta el checkbox
                checkbox.click()
                break
        # Se agrega un delay de 2 segundos para la visualizacion del resultado
        time.sleep(2)

# flujo 2
        # Se obtienen los items del menu de la pagina
        itemsdp = self.driver.find_elements(By.ID, "item-8")
        # Se recorre cada item
        for item in itemsdp:
            # Se verifica si el texto del item es igual a "Dynamic Properties"
            if item.text == "Dynamic Properties":
                # Se hace scroll hasta el item
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                # Se hace clic hasta el item
                item.click()
                break

        # Se hace una pausa de 5 segundos para habilitar el boton
        espera_boton = WebDriverWait(self.driver, 5, poll_frequency=1).until(lambda d: d.find_element(By.ID, "enableAfter"))
        # Se hace clic en el boton habilitado
        espera_boton.click()
        # Se agrega un delay de 2 segundos para la visualizacion del resultado
        time.sleep(2)

# flujo 3
        # Se obtienen los items del menu de la pagina
        itemswt = self.driver.find_elements(By.ID, "item-3")
        # Se recorre cada item
        for item in itemswt:
            # Se verifica si el texto del item es igual a "Web Tables"
            if item.text == "Web Tables":
                # Se hace scroll hasta el item
                self.driver.execute_script("arguments[0].scrollIntoView(true)", item)
                # Se hace clic en el item
                item.click()
                break

        # Se obtiene el boton de eliminar el registro de la primera fila
        borrar_boton = self.driver.find_element(By.ID, "delete-record-1")
        # Se hace scroll hasta el boton
        self.driver.execute_script("arguments[0].scrollIntoView(true)", borrar_boton)
        # Se hace clic en el boton
        borrar_boton.click()

        # Se obtiene el boton de agregar registro
        agregar_boton = self.driver.find_element(By.ID, "addNewRecordButton")
        # Se hace scroll hasta el boton
        self.driver.execute_script("arguments[0].scrollIntoView(true)", agregar_boton)
        # Se hace clic en el boton
        agregar_boton.click()

        # Se espera que se abra el modal en donde esta el formulario
        open_modal = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.ID,"registration-form-modal"))
        # Se agrega un delay de 2 segundos para la visualizacion del resultado
        time.sleep(2)
        # Se verifica que el modal se haya abierto
        assert open_modal.text == 'Registration Form' #da error, no sé por qué

        # Se obtiene el input de primer nombre del formulario
        input_firstname = self.driver.find_element(By.ID, "firstName")
        # Se ingresa el texto "Iovana" en el input
        input_firstname.send_keys("Iovana")
        # Se obtiene el input de apellido del formulario
        input_lastname = self.driver.find_element(By.ID, "lastName")
        # Se ingresa el texto "Miranda" en el input
        input_lastname.send_keys("Miranda")
        # Se obtiene el input de email del formulario
        input_email = self.driver.find_element(By.ID, "userEmail")
        # Se ingresa el texto "cmiranda@bi.com.gt" en el input
        input_email.send_keys("cmiranda@bi.com.gt")
        # Se obtiene el input de edad del formulario
        input_age = self.driver.find_element(By.ID, "age")
        # Se ingresa el texto "25" en el input
        input_age.send_keys("25")
        # Se obtiene el input de salario del formulario
        input_salary = self.driver.find_element(By.ID, "salary")
        # Se ingresa el texto "8000" en el input
        input_salary.send_keys("8000")
        # Se obtiene el input de departamento del formulario
        input_department = self.driver.find_element(By.ID, "department")
        # Se ingresa el texto "Guatemala" en el input
        input_department.send_keys("Guatemala")

        # Se obtiene el boton de enviar del formulario
        enviar_boton = self.driver.find_element(By.ID, "submit")
        # Se hace scroll hasta el boton
        self.driver.execute_script("arguments[0].scrollIntoView(true)", enviar_boton)
        # Se hace clic en el boton
        enviar_boton.click()
        # Se agrega un delay de 2 segundos para la visualizacion del resultado
        time.sleep(2)
        # verificacion = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.CLASS_NAME,"col-12.mt-4.col-md-6"))

# flujo 4
        # Se recorrer los elementos de la pagina, el menu de la izquierda
        elementos = self.driver.find_elements(By.CLASS_NAME, "header-wrapper")
        # Se recorre cada item
        for elemento in elementos:
            # Se verifica si el texto del item es igual a "Elements"
            if elemento.text == "Elements\n ":
                # Se hace scroll hasta el item
                # self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                # Se hace clic en el item
                elemento.click()
            # Se verifica si el texto del item es igual a "Forms"
            if elemento.text == "Forms\n ":
                # Se hace scroll hasta el item
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                # Se hace clic en el item
                elemento.click()
                break

        # Se agregan 3 segundos de espera para que se cargue la pagina
        time.sleep(3)
        # Se obtienen los items del menu de la pagina
        elemetosforms = self.driver.find_elements(By.ID, "item-0")
        # Se recorre cada item
        for elementoform in elemetosforms:
            # Se verifica si el texto del item es igual a "Practice Form"
            if elementoform.text == 'Practice Form':
                # Se hace scroll hasta el item
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elementoform)
                # Se hace clic en el item
                elementoform.click()
                break

        # Se obtiene el input de primer nombre del formulario
        input_firstname4 = self.driver.find_element(By.ID, "firstName")
        # Se ingresa el texto "Claudia Iovana" en el input
        input_firstname4.send_keys("Claudia Iovana")

        # Se obtiene el input de apellido del formulario
        input_lastname4 = self.driver.find_element(By.ID, "lastName")
        # Se ingresa el texto "Miranda Alvarez" en el input
        input_lastname4.send_keys("Miranda Alvarez")

        # Se obtiene el input de email del formulario
        input_email4 = self.driver.find_element(By.ID, "userEmail")
        # Se ingresa el texto "cmiranda@bi" en el input
        input_email4.send_keys("cmiranda@bi.com.gt")

        # Se obtiene los radiobuttons de genero del formulario
        genders = self.driver.find_elements(By.CLASS_NAME,"custom-control-label")
        # Se recorre cada radiobutton
        for gender in genders:
            # Se verifica si el texto del radiobutton es igual a "Female"
            if gender.text == "Female":
                # Se hace scroll hasta el radiobutton
                self.driver.execute_script("arguments[0].scrollIntoView(true)", gender)
                # Se hace clic en el radiobutton
                gender.click()
                break

        # Se obtiene el input de numero de telefono del formulario
        input_movil4 = self.driver.find_element(By.ID, "userNumber")
        # Se ingresa el texto "1234567890" en el input
        input_movil4.send_keys("1234567890")

        # Se obtiene el widget de fecha de nacimiento del formulario
        input_birthday4 = self.driver.find_element(By.ID, "dateOfBirthInput")
        # Se hace clic en el widget de fecha de nacimiento
        input_birthday4.click()
        # Se obtiene el select de mes del widget de fecha de nacimiento
        input_month4 = self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        # Se hace clic en el select de mes
        input_month4.click()
        # Se obtiene el mes de 'julio' del select de mes
        month4 = input_month4.find_element(By.CSS_SELECTOR, "option[value='6']")
        # Se hace clic en el mes de 'julio'
        month4.click()
        # Se obtiene el select de año del widget de fecha de nacimiento
        input_year4 = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
        # Se hace clic en el select de año
        input_year4.click()
        # Se obtiene el año de '1998' del select de año
        year4 = input_year4.find_element(By.CSS_SELECTOR, "option[value='1998']")
        # Se hace scroll hasta el año de '1998'
        self.driver.execute_script("arguments[0].scrollIntoView(true)", year4)
        # Se hace clic en el año de '1998'
        year4.click()
        # Se obtiene el dia '28' del widget de fecha de nacimiento
        input_day = WebDriverWait(self.driver, timeout=10, poll_frequency=2).until(lambda d: d.find_element(By.CSS_SELECTOR, "div[class='react-datepicker__day react-datepicker__day--028']"))
        # Se hace scroll hasta el dia '28'
        self.driver.execute_script("arguments[0].scrollIntoView(true)", input_day)
        # Se hace clic en el dia '28'
        input_day.click()

        # Se obtiene el input de subject del formulario
        input_subject4 = self.driver.find_element(By.ID, "subjectsInput")
        # Se ingresa el texto "Maths" en el input
        input_subject4.send_keys("Maths")
        # Se presiona la tecla ENTER
        input_subject4.send_keys(Keys.ENTER)

        # Se obtiene el input de hobbies del formulario
        input_hobbie4 = self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
        # Se hace scroll hasta el input de hobbies
        input_hobbie4.click()

        # Se guarda la ruta de la imagen
        filePath = "/home/iova/prueba.txt";
        # Se obtiene el input de picture del formulario
        input_picture4 = self.driver.find_element(By.ID, "uploadPicture")
        # Se ingresa la ruta de la imagen en el input
        input_picture4.send_keys(filePath)

        # Se obtiene el input de direccion del formulario
        input_address4 = self.driver.find_element(By.ID, "currentAddress")
        # Se ingresa el texto "Banco Industrial Zona 4 Torre 1" en el input
        input_address4.send_keys("Banco Industrial Zona 4 Torre 1")

        # Se obtiene el select de estado del formulario
        input_state4 = self.driver.find_element(By.ID, "react-select-3-input")
        # Se ingresa el texto "NCR" en el select
        input_state4.send_keys("NCR")
        # Se presiona la tecla ENTER
        input_state4.send_keys(Keys.ENTER)

        # Se obtiene el select de ciudad del formulario
        input_city4 = self.driver.find_element(By.ID, "react-select-4-input")
        # Se ingresa el texto "Delhi" en el select
        input_city4.send_keys("Delhi")
        # Se presiona la tecla ENTER
        input_city4.send_keys(Keys.ENTER)

        # Se obtiene el boton de submit del formulario
        button_submit4 = self.driver.find_element(By.ID, "submit")
        # Se envia un enter para simular un clic en el boton
        button_submit4.send_keys(Keys.ENTER)

        # Se espera a que aparezca el modal de confirmacion
        verificacion = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(lambda d: d.find_element(By.ID,"example-modal-sizes-title-lg"))
        # Se espera 2 segundos
        time.sleep(2)
        # Se verifica que el modal de confirmacion contenga el texto "Thanks for submitting the form"
        assert verificacion.text == 'Thanks for submitting the form' 

        # Se obtiene el boton de close del modal de confirmacion
        button_close4 = self.driver.find_element(By.ID, "closeLargeModal")
        # Se envia un enter para simular un clic en el boton
        button_close4.send_keys(Keys.ENTER)
        # Se espera 2 segundos
        time.sleep(2)

# flujo 5
        # Se recorrer los elementos de la pagina, el menu de la izquierda
        for elemento in elementos:
            # Se verifica que el elemento contenga el texto "Forms"
            if elemento.text == "Forms\n ":
                # Se hace scroll hasta el elemento
                # self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                # Se hace clic en el elemento
                elemento.click()
            # Se verifica que el elemento contenga el texto "Practice Form"
            if elemento.text == "Book Store Application\n ":
                # Se hace scroll hasta el elemento
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elemento)
                # Se hace clic en el elemento
                elemento.click()
                break

        # Se espera 3 segundos
        time.sleep(3)
        # Se obtiene los elementos del nuevo menu de la izquierda
        elemetosbooks = self.driver.find_elements(By.ID, "item-2")
        # Se recorre los elementos del nuevo menu de la izquierda
        for elementobook in elemetosbooks:
            # Se verifica que el elemento contenga el texto "Book Store"
            if elementobook.text == 'Book Store':
                # Se hace scroll hasta el elemento
                self.driver.execute_script("arguments[0].scrollIntoView(true)", elementobook)
                # Se hace clic en el elemento
                elementobook.click()
                break
        # Se espera 2 segundos
        time.sleep(2)
        # Se hace un scroll
        self.driver.execute_script("window.scrollTo(0, 0)")
        # Se obtiene el input de search del formulario
        input_search5 = self.driver.find_element(By.ID, "searchBox")
        # Se hace clic en el input
        input_search5.click()
        # Se ingresa el texto "Understanding ECMAScript 6" en el input
        input_search5.send_keys("Understanding ECMAScript 6")

        # Se obtiene el elemento de la pagina que contiene el texto "Understanding ECMAScript 6"
        clic_serch5 = self.driver.find_element(By.LINK_TEXT, "Understanding ECMAScript 6")
        # Se hace clic en el elemento
        clic_serch5.click()
        # Se espera 5 segundos
        time.sleep(5)

        # Se obtiene el elemento de la pagina que tiene el css "label[class='form-label']"
        clic_web5 = self.driver.find_elements(By.CSS_SELECTOR, "label[class='form-label']")
        # Se guarda la pagina actual en la variable paginaactual
        paginaactual = self.driver.current_window_handle
        # Se guarda la pagina actual en la variable nuevapagian, con el fin de inicializarla
        nuevapagina = self.driver.current_window_handle
        # Se recorre los elementos de la pagina
        for clic in clic_web5:
            # Se verifica que el elemento contenga el texto "https://leanpub.com/understandinges6/read"
            if clic.text == "https://leanpub.com/understandinges6/read":
                # Se hace scroll hasta el elemento
                self.driver.execute_script("arguments[0].scrollIntoView(true)", clic)
                # Se hace clic en el elemento
                clic.click()
                break
        # Se guarda la pagina actual en la variable nuevapagina
        nuevapagina = self.driver.window_handles[1]
        # Se cambia a la nueva pagina
        self.driver.switch_to.window(nuevapagina)
        # Se espera 10 segundos
        time.sleep(10)
        # Se cierra la nueva pagina
        self.driver.close()
        # Se cambia a la pagina actual
        self.driver.switch_to.window(paginaactual)
        # Se espera 2 segundos
        time.sleep(2)

        # Se obtiene el boton de back del formulario
        button_back5 = self.driver.find_element(By.ID, "addNewRecordButton")
        # Se envia un enter para simular un clic en el boton
        button_back5.send_keys(Keys.ENTER)
        


a = TestFlujoCompleto()

a.runFormulario()

input("Presione para continuar")