# Organización de Pruebas para "Frozen Space"

Estructuramos la estrategia de calidad dividiendo la arquitectura de Frozen Space en tres módulos funcionales y lógicos. Dado que este es un entorno diseñado para simular una aplicación web de la vida real, esta agrupación nos permitirá asignar eficientemente los enfoques de caja negra, caja blanca y pruebas exploratorias.

## 1. Módulo de Acceso y Autenticación (Login)
* **Componentes:** Formularios de inicio de sesión, mecanismos de seguridad y gestión de sesiones de usuario.
* **Enfoque de prueba:** Este es nuestro candidato principal para la automatización de regresión. Al ser un flujo repetitivo y crítico, el Automation QA utilizará el repositorio hermano "Testing Frozen Space" implementando Selenium, Python y Behave. Aplicaremos BDD (Desarrollo Guiado por Comportamiento) redactando los escenarios en formato Gherkin para interactuar con selectores clave como `#login-btn`.

## 2. Módulo de Blog y Gestión de Contenido
* **Componentes:** Visualización de posts, navegación interna e interacción del usuario con el blog.
* **Enfoque de prueba:** Requiere un enfoque híbrido. El Tester QA ejecutará pruebas funcionales y exploratorias para evaluar la usabilidad en el entorno local (Vite). Simultáneamente, el Automation QA diseñará pruebas automatizadas apuntando a elementos como `#blog-title` e implementará scripts en Python para la verificación de enlaces, recorriendo la página para detectar automáticamente códigos de error 404 y asegurar la integridad de la navegación.

## 3. Módulo de Backend y Base de Datos (MSSQL)
* **Componentes:** API desarrollada en Node.js/Express y conexión a la base de datos Microsoft SQL Server.
* **Enfoque de prueba:** Pruebas de integración y validación de datos. Nos centraremos en asegurar que la información generada desde el Frontend se persista correctamente mediante la Autenticación de Windows configurada localmente. Se sugiere utilizar SQL Server Management Studio (SSMS) para monitorear la creación de usuarios y posts.
