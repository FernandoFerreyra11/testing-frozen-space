# Tareas QA para el Plan de Mantenimiento (Cronograma de 20 Días)

Para garantizar el cumplimiento de los objetivos de calidad en Frozen Space, se distribuyen las tareas operativas de la siguiente manera:

## Etapa 1: Planificación y Análisis de Riesgos (Días 1-3)
* **Leader QA:** Definir los objetivos de calidad, documentar los riesgos de infraestructura (ej. problemas con el puerto `5173`) y establecer los criterios de entrada.
* **Automation QA:** Clonar el repositorio "Testing Frozen Space", instalar las dependencias vía `requirements.txt` y verificar que el `webdriver-manager` funcione correctamente en el entorno local.
* **Tester QA:** Configurar el entorno del repositorio principal: instalar Node.js, configurar las variables en el `.env`, inicializar la base de datos SQL Server y verificar que la app levante con `npm run dev:all`.

## Etapa 2: Pruebas Exploratorias y Diseño DGC (BDD)(Días 4-7)
* **Leader QA:** Validar con los stakeholders que el alcance de las pruebas cubra adecuadamente los módulos de Registro-Login y Blog.
* **Automation QA:** Redactar los archivos `.feature` en la carpeta `features/` utilizando Gherkin, definiendo claramente los selectores a utilizar (como `#login-btn`).
* **Tester QA:** Iniciar la ejecución de pruebas exploratorias sobre la aplicación corriendo en `localhost:5173`, aprendiendo el comportamiento del sistema y documentando posibles anomalías de usabilidad.

## Etapa 3: Implementación y Preparación (Días 8-15)
* **Leader QA:** Supervisar la gestión de configuración asegurando que ambos repositorios (aplicación y testing) se mantengan sincronizados sin conflictos.
* **Automation QA:** Desarrollar los pasos lógicos en `features/steps/steps.py` mediante decoradores de Behave y estructurar las clases en la carpeta `pages/` aplicando el patrón Page Object Model.
* **Tester QA:** Utilizar SSMS para inyectar datos de prueba controlados en MSSQL (usuarios base, posts predeterminados) que servirán tanto para las pruebas manuales como para que los scripts de automatización interactúen con ellos.

## Etapa 4: Ejecución y Gestión de Defectos (Días 16-19)
* **Leader QA:** Monitorizar la ejecución diaria. Gestionar el ciclo de vida de los defectos bloqueantes detectados.
* **Automation QA:** Ejecutar la suite completa mediante el comando por lotes `run_tests.bat`. Al finalizar, analizar el archivo `reporte.csv` generado para distinguir entre verdaderos defectos de la aplicación o elementos no encontrados (Error: Elemento no encontrado) por cambios en los selectores.
* **Tester QA:** Ejecutar los casos manuales complementarios, realizar las pruebas de confirmación sobre los bugs corregidos y emitir informes de defectos detallados.

## Etapa 5: Compleción y Cierre (Día 20)
* **Leader QA:** Consolidar las métricas de estado y duración extraídas del `reporte.csv` para redactar el informe de compleción de prueba y liderar la retrospectiva del equipo.
* **Automation QA:** Estabilizar el código de Selenium/Behave, asegurando que utilicen buenas prácticas (`environment.py` para setup/teardown) y realizar el push final al repositorio.
* **Tester QA:** Documentar el flujo funcional definitivo de Frozen Space y las lecciones aprendidas sobre su base de datos local.
