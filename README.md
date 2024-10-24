
# Backend - Blog API

## Descripción

Este es el backend de una aplicación de blog construida con **Flask**, **SQLAlchemy** y **PostgreSQL**. La API permite gestionar las entradas de blog mediante operaciones CRUD (crear, leer, actualizar, eliminar). También se implementa la autenticación mediante JWT para el administrador del blog.

## Requisitos Previos

- **Python** (versión 3.10 o superior)
- **PostgreSQL**
- **pip** (el gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/oliver0709/OVS-API-BlogBackend.git
   ```
2. Navega al directorio del proyecto:

```bash
cd OVS-API-BlogBackend
```
3. Crea y activa un entorno virtual:

```bash

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
4. Instala las dependencias:

```bash
pip install -r requirements.txt
```
5. Configura las variables de entorno en un archivo .env en la raíz del proyecto:

```bash
FLASK_APP=run.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=postgresql://usuario:contraseña@servidor:puerto/nombre_base_datos
JWT_SECRET_KEY=tu_clave_secreta
```
6. Inicializa la base de datos y aplica las migraciones:

```bash
flask db upgrade
```
7. Ejecuta el servidor localmente:

```bash
flask run
```
Esto iniciará el servidor en http://localhost:5000.


## Endpoints de la API

### Autenticación

- POST /auth/login: Inicia sesión y devuelve un token JWT.

Cuerpo de la solicitud:
```json
{
  "email": "youremail@email.com",
  "password": "your password"
}
```
- POST `/auth/register`: Registra un nuevo usuario (solo el admin puede hacerlo).

### Blogs
- GET `/portfolio/portfolio_blogs`: Obtiene todas las entradas de blog.
- GET `/portfolio/portfolio_blogs/<id>`: Obtiene una entrada de blog específica.
- POST `/portfolio/portfolio_blogs`: Crea una nueva entrada de blog.
- PATCH `/portfolio/portfolio_blogs/<id>`: Actualiza una entrada de blog existente.
- DELETE `/portfolio/portfolio_blogs/<id>`: Elimina una entrada de blog.

## Despliegue en Render

Para desplegar el backend en Render:

1. Sube el proyecto a un repositorio GitHub.

2. Configura una nueva aplicación en Render.com conectada a tu repositorio.

3. Configura las variables de entorno necesarias en Render (como SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY).

4. plica las migraciones en la base de datos remota:

```bash
flask db upgrade
```
5. Asegúrate de que el servidor se ejecuta usando Gunicorn:

```bash
gunicorn run:app
```
## Dependencias Principales
- Flask: Microframework de Python para crear aplicaciones web.
- Flask-JWT-Extended: Extensión de Flask para la - autenticación con JWT.
- Flask-SQLAlchemy: ORM para interactuar con la base de datos.
- Flask-Migrate: Manejo de migraciones de la base de datos.
- PostgreSQL: Sistema de gestión de bases de datos relacional.

### Licencia

Este proyecto está bajo la licencia MIT.
