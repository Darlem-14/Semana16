# Restaurante App

Aplicación de gestión para restaurantes desarrollada en **Python** utilizando **Programación Orientada a Objetos (POO)** y una arquitectura modular que separa los datos, modelos, servicios e interfaz de usuario.

El proyecto permite gestionar productos, usuarios, pedidos y ventas mediante archivos **JSON**, manteniendo una estructura organizada y fácil de mantener.

## 📌 Características

* Inicio de sesión de usuarios.
* Manejo de roles: **administrador** y **cliente**.
* Visualización de productos disponibles.
* Creación de pedidos mediante un carrito de compra.
* Control y actualización automática del stock.
* Registro de ventas realizadas.
* Persistencia de información mediante archivos JSON.
* Organización del proyecto mediante arquitectura modular.
* Desarrollo basado en Programación Orientada a Objetos.

## 🗂️ Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

## Descripción de los módulos

### 📁 `datos/`

Contiene los archivos JSON utilizados para almacenar la información de la aplicación:

* `productos.json`: productos, precios y stock.
* `usuarios.json`: usuarios, roles y credenciales.
* `ventas.json`: registro de las ventas realizadas.

### 📁 `modelos/`

Contiene las clases principales del sistema:

* `Producto`: representa los productos del restaurante.
* `Usuario`: representa a los usuarios y sus roles.
* `Venta`: representa las ventas realizadas.

### 📁 `servicios/`

Contiene la lógica de negocio y el manejo de archivos JSON.

* `archivo_servicio.py`: lectura y escritura de archivos JSON.
* `restaurante_servicio.py`: gestión de productos, usuarios, ventas y stock.

### 📁 `ui/`

Contiene la interfaz de interacción con el usuario mediante consola:

* `login_view.py`: controla el inicio de sesión.
* `main_view.py`: muestra el menú principal y permite realizar las operaciones del sistema.

### 📄 `main.py`

Es el punto de entrada de la aplicación. Inicializa los servicios, solicita el inicio de sesión y ejecuta el menú principal.

## Funcionamiento

1. El usuario inicia sesión.
2. El sistema valida sus credenciales.
3. Se muestra el menú principal según su rol.
4. Puede consultar los productos disponibles.
5. Puede seleccionar productos y cantidades.
6. El sistema verifica el stock disponible.
7. Se registra el pedido y se actualiza el inventario.
8. Las ventas quedan almacenadas en `ventas.json`.
9. El administrador puede consultar el historial de ventas.

## Tecnologías utilizadas

* **Python 3**
* **Programación Orientada a Objetos (POO)**
* **JSON**
* **Git / GitHub**
* Arquitectura modular por capas

## Objetivo

Desarrollar una aplicación sencilla para la gestión de un restaurante, aplicando principios de **Programación Orientada a Objetos**, separación de responsabilidades, manejo de archivos y organización modular del código.

## 👨‍💻 Autor:

Darlem Jaramillo


Proyecto académico — Programación Orientada a Objetos
