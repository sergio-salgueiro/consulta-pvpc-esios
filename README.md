# consulta-pvpc-esios

Script en Python para consultar el precio de la luz (PVPC) a través de la API de ESIOS (REE) y mostrar el resultado en formato JSON por consola.

Actualmente el script:

- Consulta el indicador **1001** (PVPC) de la API de ESIOS.
- Obtiene los datos de un **intervalo de 24 horas**, desde **ayer a esta misma hora** hasta **el momento actual**.
- Muestra la respuesta completa de la API formateada por pantalla.

El fichero principal del proyecto es `pvpc.py`.

## Requisitos

- Python 3.8 o superior
- Acceso a internet
- Clave de API de ESIOS (`x-api-key`)

### Librerías de Python

Las dependencias se gestionan con `pip` mediante `requirements.txt`:

- `requests`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/sergio-salgueiro/consulta-pvpc-esios.git
   cd consulta-pvpc-esios
   ```

2. (Opcional pero recomendado) Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   # En Linux / macOS
   source venv/bin/activate
   # En Windows
   venv\Scriptsctivate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Obtención de la API key

Para usar la API de ESIOS necesitas una **API key**.

En la siguiente página oficial de ESIOS se explica cómo obtenerla y cómo usar la API:

- https://www.esios.ree.es/es/pagina/api

Sigue las instrucciones de registro y solicitud de token que se indican allí.

## Configuración de la API key

El script lee la clave de la API desde la variable de entorno `ESIOS_API_KEY`.

> Aunque en el código hay un comentario `#introduce aqui tu api KEY`, no es necesario modificar el script: basta con definir la variable de entorno.

### Linux / macOS

```bash
export ESIOS_API_KEY="tu_api_key_de_esios"
```

### Windows (PowerShell)

```powershell
setx ESIOS_API_KEY "tu_api_key_de_esios"
```

Después de esto, abre una nueva terminal para que la variable esté disponible.

## Uso

Dentro de la carpeta del proyecto, ejecuta:

```bash
python pvpc.py
```

Por defecto, el script:

- Calcula un intervalo de fechas correspondiente a **las últimas 24 horas** (desde ayer a esta misma hora hasta ahora).
- Llama a la API de ESIOS para el indicador 1001.
- Imprime por pantalla la respuesta JSON formateada.

## Personalización del intervalo de fechas

Si quieres cambiar el intervalo (por ejemplo, consultar un rango fijo de fechas), puedes editar la función `main()` en `pvpc.py`:

```python
from datetime import datetime

def main():
    """
    Define el intervalo de fechas y llama a fetch_pvpc.

    Ahora mismo está configurado para ir desde ayer hasta mañana.
    Puedes cambiar estas fechas a las que quieras.
    """
    # Ejemplo: desde ayer a esta misma hora hasta hoy a esta misma hora
    start_dt = datetime.now() - timedelta(days=1)
    end_dt = datetime.now()

    # Si quieres fechas concretas, las puedes definir así:
    # start_dt = datetime(2025, 1, 1, 0, 0, 0)
    # end_dt   = datetime(2025, 1, 2, 0, 0, 0)

    fetch_pvpc(start_dt, end_dt)
```

Modifica las fechas según tus necesidades y vuelve a ejecutar:

```bash
python pvpc.py
```

## Estructura del proyecto

```text
consulta-pvpc-esios/
├── pvpc.py            # Script principal
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Este archivo
```

