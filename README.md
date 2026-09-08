<div align="center">

# ⚡ Azure Functions URL Health Monitor

> API serverless desarrollada en Python utilizando Azure Functions para verificar en tiempo real el estado de salud de cualquier sitio web o URL (códigos de estado, disponibilidad y respuestas HTTP).

[![Azure Functions](https://img.shields.io/badge/Azure_Functions-Serverless-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Activo-success?style=flat-square)]()

</div>

---

## 🎯 Acerca del Proyecto

Este servicio backend opera bajo la arquitectura *serverless* de **Microsoft Azure Cloud**. Su función principal es recibir peticiones HTTP, procesar la URL proporcionada por el usuario mediante una función de verificación en Python (`verificar_estado_web`), y retornar un JSON estructurado con el diagnóstico exacto del enlace analizado.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Cloud / Backend:** Azure Functions (Serverless)
* **Control de Versiones:** Git & GitHub
* **Entorno de Desarrollo:** Visual Studio Code

---

## 📂 Estructura del Proyecto

| Archivo / Carpeta | Descripción |
| :--- | :--- |
| `function_app.py` | Archivo principal con las funciones HTTP de Azure y la lógica de validación. |
| `requirements.txt` | Dependencias del proyecto en Python. |
| `host.json` / `local.settings.json` | Configuraciones de ejecución local y del host de Azure Functions. |
| `Dockerfile` / `.dockerignore` | Configuración para contenedores (opcional para despliegues). |

---

## 🚀 Ejecución Local

Para poner en marcha este entorno de Azure Functions en tu máquina local:

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/maxwellb0809/monitor-python.git](https://github.com/maxwellb0809/monitor-python.git)
