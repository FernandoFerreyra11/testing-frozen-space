# Pruebas Automatizadas con Selenium, Python, Gherkin y Behave

Este proyecto proporciona una estructura completa para pruebas automatizadas de aceptación utilizando BDD (Behavior Driven Development) con Behave, Gherkin para la especificación de escenarios, Selenium para la automatización del navegador y Python como lenguaje de programación.

## Estructura del Proyecto

```text
Testing Frozen Space/
├── features/                    # Archivos .feature con escenarios Gherkin
│   ├── steps/                   # Implementaciones de los pasos en Python
│   │   ├── __init__.py
│   │   ├── steps.py             # Definiciones de pasos (Login y Registro
│   │   └── blog_steps.py        # Definiciones de pasos (Blog)
│   ├── environment.py           # Configuración de setup/teardown y reportes
│   ├── login.feature            # Feature de inicio de sesión
│   ├── register.feature         # Feature de registro de usuario
│   └── blog.feature             # Feature de creación de posts en el blog
├── pages/                       # Page Object Model
│   ├── __init__.py
│   ├── login_page.py            # Clase para la página de login
│   ├── register_page.py         # Clase para la página de registro
│   └── blog_page.py             # Clase para la página del blog
├── utils/                       # Utilidades y helpers
│   ├── __init__.py
│   ├── csv_utils.py             # Herramienta para leer datos de prueba en CSV
│   └── driver_factory.py        # Factory para crear instancias de WebDriver
├── drivers/                     # Drivers de navegador
├── requirements.txt             # Dependencias de Python
├── behave.ini                   # Configuración de Behave
├── run_tests.bat                # Script automático para correr pruebas
├── reporte.csv                  # Reporte generado tras cada ejecución
└── README.md                    # Este archivo
```

## Requisitos Previos

- Python 3.8 o superior
- Navegador web (Chrome recomendado)
- **Repositorio Principal Corriendo**: Aclaración importante: este proyecto solo abarca la automatización de QA. Para que las pruebas funcionen y encuentren los selectores (`#blog-title`, `#login-btn`, etc.), **la aplicación Frozen Space debe estar en ejecución localmente**. Asegúrate de tener el [repositorio principal de Frozen Space] descargado y ejecutándose (frontend activo mediante Vite en `localhost:5173` y su API).
- **Base de Datos (SQL Server)**: El backend principal interactúa localmente con Microsoft SQL Server mediante Autenticación de Windows. Recomendamos instalar *SQL Server Management Studio (SSMS)* o tu gestor favorito para correr los scripts de inicialización de la BD y poder monitorear los usuarios/posts que este framework de automatización va generando durante las pruebas.

## Instalación

1. Clona o descarga este proyecto
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de Pruebas

### Ejecutar todas las pruebas:
```bash
behave
```

### Ejecutar una feature específica:
```bash
behave features/login.feature
```

### Ejecutar con tags:
```bash
behave --tags @login
```

### Ejecutar en modo verbose:
```bash
behave -v
```

### Ejecutar con Script y Reporte Automático:
A través del archivo batch incluido, puedes ejecutar todas las pruebas y generar el reporte final sin comandos complejos:
```bash
.\run_tests.bat
```
📌 **Nota**: Al finalizar las pruebas (sea con el script o usando behave directamente), el entorno generará en la raíz del proyecto un archivo `reporte.csv` con métricas clave para cada escenario testado (estado, duración, errores e infraestructura).

## Escribiendo Nuevas Pruebas

### 1. Crear un archivo .feature
En la carpeta `features/`, crea un archivo con extensión `.feature`:

```gherkin
Feature: Nombre de la funcionalidad
  Como usuario
  Quiero hacer algo
  Para obtener un beneficio

  @tag
  Scenario: Descripción del escenario
    Given estoy en la página de login
    When ingreso mis credenciales
    Then debería ver el dashboard
```

### 2. Implementar los pasos
En `features/steps/steps.py`, implementa los pasos usando decoradores de Behave:

```python
from behave import given, when, then
from pages.login_page import LoginPage

@given('estoy en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()

@when('ingreso mis credenciales')
def step_impl(context):
    context.login_page.enter_username("usuario")
    context.login_page.enter_password("password")
    context.login_page.click_login()

@then('debería ver el dashboard')
def step_impl(context):
    assert context.login_page.is_dashboard_visible()
```

### 3. Crear Page Objects
En la carpeta `pages/`, crea clases que representen las páginas web:

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def navigate_to_login(self):
        self.driver.get("https://example.com/login")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_visible(self):
        # Implementar verificación
        return True
```

## Configuración del WebDriver

El proyecto utiliza `webdriver-manager` para gestionar automáticamente los drivers de navegador. No es necesario descargar drivers manualmente.

## Mejores Prácticas

1. **Page Object Model**: Usa clases separadas para cada página web
2. **Separación de Concerns**: Mantén los pasos Gherkin simples y la lógica en Page Objects
3. **Reutilización**: Crea steps genéricos que puedan ser reutilizados
4. **Tags**: Usa tags para organizar y ejecutar subconjuntos de pruebas
5. **Setup/Teardown**: Usa `environment.py` para inicializar y limpiar recursos

## Troubleshooting

### Error: WebDriver no encontrado
Asegúrate de que `webdriver-manager` esté instalado y ejecuta:
```bash
webdriver-manager update
```

### Error: Elemento no encontrado
Verifica los selectores CSS/XPath en tus Page Objects. Los elementos pueden cambiar en la aplicación.

### Tests fallan en CI/CD
Asegúrate de que el navegador esté disponible en el entorno de CI. Considera usar headless mode.

## Contribución

Siéntete libre de contribuir mejoras a esta estructura de pruebas.