# Proyecto Tienda 🛒

Aplicación de escritorio desarrollada en **Python** con interfaz gráfica usando **Tkinter** para la gestión de empleados y funcionalidades de tienda.

## 📂 Estructura del proyecto

PROYECTO_TIENDA/
├── assets/ # Recursos gráficos (iconos, imágenes, etc.)
├── funcionalidades/ # Funciones principales de la aplicación
│ └── funcionalidades_pro.py
├── utils/ # Utilidades y base de datos
│ ├── init.py
│ ├── base_de_datos.db
│ └── utils.py
├── venv/ # Entorno virtual (no se sube a GitHub)
├── main.py # Punto de entrada de la aplicación
├── requirements.txt # Dependencias del proyecto
├── test_consola.py # Script de pruebas en consola
└── README.md # Este archivo

## 🚀 Características

- Interfaz gráfica amigable usando **Tkinter**.
- Conexión a base de datos **SQLite** para manejo de información.
- Módulos organizados en carpetas (`funcionalidades`, `utils`).
- Exportable a `.exe` usando **PyInstaller**.
- Código comentado y estructurado para facilitar mantenimiento.

## 🖥️ Requisitos

- Python 3.10 o superior  
- Librerías listadas en `requirements.txt`

Instalar dependencias:

```bash
pip install -r requirements.txt
▶️ Ejecución en modo desarrollo
bash
Copiar
Editar
python main.py
📦 Generar ejecutable (.exe)
Usando PyInstaller:

bash
Copiar
Editar
pyinstaller --onefile --windowed --icon=assets/icono_main.ico main.py
El archivo .exe aparecerá en la carpeta dist/.

📄 Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito al autor original.

Desarrollado con ❤️ por Luis Enrique Rondón

yaml
Copiar
Editar

---

## 2️⃣ `.gitignore`

Crea un archivo llamado `.gitignore` en la raíz y pon esto adentro:  

```gitignore
# Entorno virtual
venv/
ENV/
env/

# Archivos compilados de Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Archivos de PyInstaller
build/
dist/
*.spec

# Archivos del sistema
.DS_Store
Thumbs.db

# Ejecutables
*.exe

# Base de datos 
# utils/base_de_datos.db

NOTA FINAL: Este proyecto no esta terminado, volvere pronto luego de estudiar un poco mas ❤️
