# Selenium

[Tutorial completo en Youtube](https://www.youtube.com/playlist?list=PLjM3-neCG6qx4RFeq2X-TpWS_tJTk1qZP)

[Selenium oficial](https://www.selenium.dev/)

Used to Scrape web sites with Javascript.

```
$ pip install selenium
```

Selenium requires a driver to interface with the chosen browser. To consult de Chrome version `about://version`. I Downloaded de version 98 (my case). Locate de file `.exe` beside the script to execute.
```
https://sites.google.com/chromium.org/driver/downloads
```



Hay una nueva forma de llamar el driver, aunque lo hace muy lento al tener que descargar el driver cada vez que ejecuta el código.

```
$ pip install webdriver-manager
```
```py
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

aún así, se recomienda añadir un **Service** al llamar el driver
```py
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

La forma más rápida que encontré para ejecutar el código es
```py
chromedriver = 'ruta/absoluta/chromedriver.exe'
driver = webdriver.Chrome(service=Service(chromedriver))
```


To generate reports

```
pip install pyunitreport
```

## WebDriver Class

Propiedad/Atributo | Descripción
------------------ | -----------
`current_url`	| Obtiene la URL del sitio en la que se encuentra el navegador
`current_window_handle` | Obtiene la referencia que identifica a la ventana activa en ese momento
`name` | Obtiene el nombre del navegador subyacente para la instancia activa
`orientation`	| Obtiene la orientación actual del dispositivo móvil
`page_source`	| Obtiene el código fuente disponible del sitio web
`title` | Obtiene el valor de la etiqueta \<title\> del sitio web
------------------ | -----------
`get()` | carga la url indicada y navega hacia ella
`maximize_window()` | Maximiza la ventana del navegador
`back()` | Va una página atrás
`forward()` | Va una página adelante
`refresh()` | 
`switch_to.` | 
`close()` | Cierera la ventana actual
`quit()` | Cierra el driver de navegación y todas sus ventanas

In summary ensure that `Quit()` or `Dispose()` is called before exiting the program, and don't use the `Close()` method unless you're sure of what you're doing.

 ## WebElement Class

Propiedad/Atributo	| Descripción
------------------ | -----------
`size` | Obtiene el tamaño del elemento
`tag_name` | Obtiene el nombre de la etiqueta HTML del elemento
`text` | Obtiene el texto del elemento
 ------------------ | -----------
`clear()` | Limpia el contenido de un **textarea**
`click()` | Hace clic en el elemento
`get_attribute(name/value)` | Obtiene el valor del atributo de un elemento
`is_displayed()` | Verifica si el elemento está a la vista al usuario
`is_enabled()` | Verifica si el elemento está habilitado
`is_selected()` | Verifica si el elemento está seleccionado (checkbox o radio button)
`send_keys(value)` | Simula escribir o presionar teclas en un elemento
`submit()` | Envía un formulario o confirmación en un text area
`value_of_css_property(property_name)` | Obtiene el valor de una propiedad CSS del elemento

## Waits

[Waits](https://selenium-python.readthedocs.io/waits.html)

* **Explicit wait** makes WebDriver wait for a certain condition to occur before proceeding further with execution. 
* **Implicit wait** makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

> Warning: Do not mix implicit and explicit waits. Doing so can cause unpredictable wait times.