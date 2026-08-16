# Frecuencias-812

Generador automático de la "Frecuencia del Día" y notificador.  
Este proyecto selecciona o genera una frecuencia (MHz) y publica un mensaje (embed) en un canal (por ejemplo vía webhook de Discord). Está pensado para ejecutarse periódicamente (p. ej. diariamente) mediante GitHub Actions o un cron local.

## Captura de ejemplo
La siguiente imagen muestra el tipo de mensaje/embed que se genera y publica (Image2):
![Ejemplo de frecuencia publicada] <img width="495" height="232" alt="image" src="https://github.com/user-attachments/assets/48c02350-982e-45bb-8454-a868d6fc6985" />


## Características
- Genera una frecuencia diaria (en MHz).
- Publica el resultado como mensaje formateado (embed) en un servicio externo (ej. Discord) usando un webhook.
- Fácil de ejecutar localmente o programar en GitHub Actions para ejecución automática.

## Estructura del repositorio
- `main.py` — script principal que genera la frecuencia y realiza el post.
- `requirements.txt` — dependencias (por ejemplo `requests`).
- `.github/workflows/radio.yml` — workflow de ejemplo para ejecución programada.
- `images/` — carpeta para capturas y ejemplos (añade `imagen2.png` aquí).

## Requisitos
- Python 3.8+  
- Conexión a Internet para enviar los webhooks (si se usa envío remoto).

## Instalación (local)
1. Clona el repositorio:
   git clone https://github.com/BendeRCL/frecuencias-812
2. Entra en la carpeta:
   cd frecuencias-812
3. Crea y activa un entorno virtual (recomendado):
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .\.venv\Scripts\activate   # Windows (PowerShell)
4. Instala dependencias:
   pip install -r requirements.txt

## Configuración
El script necesita al menos la URL del webhook para publicar (si vas a publicar). Puedes configurarlo usando variables de entorno o un archivo `.env` (si tu `main.py` lo soporta).

Ejemplo (exportar variable de entorno):
- Linux / macOS:
  export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
- Windows (PowerShell):
  $env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."

Variables recomendadas:
- `DISCORD_WEBHOOK_URL` — webhook para enviar el embed.
- `TIMEZONE` (opcional) — zona horaria para la fecha publicada (p. ej. "America/Santiago").
- `DRY_RUN` (opcional) — si está implementado, cuando esté en `true` no envía el webhook y solo imprime el resultado.

