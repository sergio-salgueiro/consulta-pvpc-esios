import os
import json
import requests
from datetime import datetime, timedelta


# -------------------------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------------------------

def to_iso_utc(dt: datetime) -> str:
    """
    Convierte un objeto datetime a cadena en formato ISO 8601 UTC,
    que es el formato que espera la API de ESIOS.
    Ejemplo: 2025-01-01T00:00:00Z
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_pvpc(start_dt: datetime, end_dt: datetime) -> None:
    """
    Realiza la llamada a la API de ESIOS para el indicador 1001
    en el intervalo [start_dt, end_dt] y printea el resultado.

    :param start_dt: fecha/hora de inicio del intervalo
    :param end_dt: fecha/hora de fin del intervalo
    """
    base_url = "https://api.esios.ree.es/indicators/1001"

    # Parámetros de la query con las fechas en formato ISO
    params = {
        "start_date": to_iso_utc(start_dt),
        "end_date": to_iso_utc(end_dt)
    }

    #introduce aqui tu api KEY
    api_key = os.getenv("ESIOS_API_KEY", "")

    headers = {
        "Accept": "application/json; application/vnd.esios-api-v1+json",
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=10)

        # Lanza excepción si el código no es 2xx
        response.raise_for_status()

        data = response.json()

        # Printeamos el resultado completo de la API, formateado
        print(json.dumps(data, indent=2, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        # Errores de conexión / timeout / HTTP no exitoso
        print(f"Error en la llamada a la API: {e}")
        # Si tenemos respuesta, mostramos info adicional
        if 'response' in locals() and response is not None:
            print(f"Código de estado HTTP: {response.status_code}")
            print(f"Cuerpo de la respuesta: {response.text}")


# -------------------------------------------------------------------
# Punto de entrada del script
# -------------------------------------------------------------------

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


if __name__ == "__main__":
    main()
