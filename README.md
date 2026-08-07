# API REST de Pokémon

## Descripción

Esta es una API REST desarrollada con **Python** y **Flask** que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una colección de Pokémon almacenada en memoria.

La información se mantiene únicamente mientras la aplicación está en ejecución. Al reiniciar el servidor, los datos se pierden.

---

# Requisitos

- Python 3.10 o superior
- Windows (para utilizar el archivo `instalar.bat`)

---

# Instalación

1. Descargar o clonar el proyecto.

2. Ejecutar el archivo:

```text
instalar.bat
```

Este archivo realiza automáticamente:

- Creación del entorno virtual.
- Instalación de las dependencias.
- Preparación del proyecto.

---

# Ejecutar la API

Una vez finalizada la instalación, ejecutar:

```bash
python app.py
```

Si todo funciona correctamente aparecerá un mensaje similar a:

```text
 * Running on http://127.0.0.1:5000
```

La API quedará disponible en:

```text
http://127.0.0.1:5000
```

---

# Endpoints

## Inicio

### GET /

Verifica que la API se encuentre funcionando.

**Respuesta**

```text
API Pokemon funcionando
```

---

## Obtener todos los Pokémon

### GET /pokemons

Devuelve la lista completa de Pokémon registrados.

**Respuesta**

```json
[
    {
        "id": 1,
        "nombre": "Pikachu",
        "tipo": "Eléctrico"
    }
]
```

---

## Crear un Pokémon

### POST /pokemons

Crea un nuevo Pokémon.

**Body (JSON)**

```json
{
    "id": 1,
    "nombre": "Pikachu",
    "tipo": "Eléctrico"
}
```

**Respuesta**

```json
{
    "mensaje": "Pokemon creado correctamente",
    "pokemon": {
        "id": 1,
        "nombre": "Pikachu",
        "tipo": "Eléctrico"
    }
}
```

---

## Obtener un Pokémon

### GET /pokemons/{id}

Obtiene un Pokémon según su identificador.

**Ejemplo**

```text
GET /pokemons/1
```

**Respuesta**

```json
{
    "id": 1,
    "nombre": "Pikachu",
    "tipo": "Eléctrico"
}
```

Si no existe:

```json
{
    "mensaje": "Pokemon no encontrado"
}
```

---

## Actualizar un Pokémon

### PUT /pokemons/{id}

Actualiza los datos de un Pokémon existente.

**Ejemplo**

```text
PUT /pokemons/1
```

**Body**

```json
{
    "nombre": "Raichu",
    "tipo": "Eléctrico"
}
```

**Respuesta**

```json
{
    "mensaje": "Pokemon actualizado",
    "pokemon": {
        "id": 1,
        "nombre": "Raichu",
        "tipo": "Eléctrico"
    }
}
```

---

## Eliminar un Pokémon

### DELETE /pokemons/{id}

Elimina un Pokémon.

**Ejemplo**

```text
DELETE /pokemons/1
```

**Respuesta**

```json
{
    "mensaje": "Pokemon eliminado"
}
```

---

# Códigos de respuesta

| Código | Descripción |
|---------|-------------|
| 200 | Operación realizada correctamente |
| 201 | Recurso creado correctamente |
| 404 | Pokémon no encontrado |

---

# Herramientas recomendadas para probar la API

Se puede utilizar cualquiera de las siguientes herramientas:

- Postman
- Insomnia
- Thunder Client (Visual Studio Code)
- cURL

---

# Estructura del proyecto

```text
Proyecto/
│
├── app.py
├── instalar.bat
├── requirements.txt
├── README.md
└── venv/
```

---

# Dependencias

```text
Flask
```

También pueden instalarse manualmente mediante:

```bash
pip install -r requirements.txt
```