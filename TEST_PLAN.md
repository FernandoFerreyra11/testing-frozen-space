# Plan de Pruebas de Mantenimiento: Plataforma "Frozen Space"

## 1. Introducción y Alcance
El objetivo es realizar pruebas exhaustivas sobre la plataforma local Frozen Space, validando tanto el Frontend (Vite) como el Backend (Node.js/MSSQL). El enfoque combina el descubrimiento de defectos mediante pruebas exploratorias manuales y la consolidación técnica mediante la automatización del framework del repositorio "Testing Frozen Space". 

> [!NOTE]
> Para una visión detallada de la segmentación modular y los enfoques técnicos (caja negra, blanca y exploratoria), consulte el documento: [ESTRATEGIA_DE_PRUEBAS.md](file:///c:/testingfrozenSpace/ESTRATEGIA_DE_PRUEBAS.md).
>
> Para el cronograma detallado de tareas y la distribución de responsabilidades en un ciclo de 20 días, consulte: [CRONOGRAMA_DE_PRUEBAS.md](file:///c:/testingfrozenSpace/CRONOGRAMA_DE_PRUEBAS.md).

### 1.1 Funcionalidades bajo prueba
* **Autenticación:** Inicio de sesión y registro de usuarios.
* **Módulo de Blog:** Creación de posts (con límite de caracteres y soporte para múltiples imágenes), visualización de publicaciones y sistema de comentarios restringido.
* **Navegación UI:** Verificación de la barra de navegación persistente.

## 2. Roles y Responsabilidades
* **Leader QA (Gestión de Prueba):** Responsable de la planificación, control de riesgos, monitorización del avance (comparando el plan contra la ejecución real) y elaboración del informe de compleción final.
* **Automation QA (Rol Técnico):** Encargado de la implementación del marco de automatización utilizando el modelo Page Object Model (POM). Deberá diseñar guiones con Behave y Python, asegurando la cobertura de funciones críticas bajo el enfoque DGC.
* **Tester QA (Rol de Ingeniería):** Responsable de la configuración del entorno de prueba local (variables `.env`, ejecución dual con `npm run dev:all`), ejecución de pruebas exploratorias en `localhost:5173` y documentación estructurada de defectos.

## 3. Estrategia y Enfoque de Prueba
* **Prueba Exploratoria:** Para evaluar la calidad desde la perspectiva del usuario final interactuando con las funcionalidades reales del blog y autenticación.
* **Automatización de Regresión:** Centrada en flujos críticos para ahorrar tiempo, garantizando que los cambios en el código no rompan la funcionalidad base.
* **Pruebas de Confirmación:** Verificación estricta de que los defectos reportados en iteraciones previas hayan sido mitigados con éxito.

## 4. Entorno de Pruebas y Stack Tecnológico
* **Framework de Automatización:** Python 3, Behave (BDD), Selenium WebDriver.
* **Aplicación Base (SUT - System Under Test):** Node.js (Express), Frontend (Vite), SQL Server (Autenticación de Windows local).
* **Reportes:** Generación de métricas de ejecución (tiempo, métricas de éxito/falla, entorno) mediante la salida tabular en `.csv`.

## 5. Riesgos Identificados
* **De Entorno:** Que la aplicación base de Frozen Space no esté ejecutándose en `localhost:5173` durante la ejecución automatizada, lo que causaría que Selenium no encuentre los selectores.
* **De Producto:** Fallas de conexión con la base de datos local debido a una incorrecta configuración de las credenciales en el archivo `.env` o problemas con la Autenticación de Windows en MSSQL.
* **De Automatización:** Posible desactualización de `chromedriver` frente a la versión del navegador instalada en la máquina de ejecución.

## 6. Criterios de Salida
El ciclo concluirá al obtener el 100% de ejecución de los escenarios definidos en el framework de automatización, la generación exitosa del `reporte.csv` sin fallos críticos y la resolución de defectos de severidad alta en la UI y API.
