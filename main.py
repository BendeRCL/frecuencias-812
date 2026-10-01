import requests
import os
from datetime import datetime
from zoneinfo import ZoneInfo

WEBHOOK = os.getenv("WEBHOOK")

# Hora de Chile
fecha = datetime.now(ZoneInfo("America/Santiago"))

# Día del mes (01 al 31)
dia = fecha.strftime("%d")

# Frecuencia fija según el día
frecuencia = f"854.{dia}"

embed = {
    "title": "📻 Frecuencia del Día",
    "description": "La frecuencia asignada para las comunicaciones de hoy es:",
    "color": 3447003,
    "fields": [
        {
            "name": "📡 Frecuencia",
            "value": f"**{frecuencia} MHz**",
            "inline": False
        },
        {
            "name": "📅 Fecha",
            "value": fecha.strftime("%d/%m/%Y"),
            "inline": False
        }
    ],
    "footer": {
        "text": "Sistema Automático de Frecuencias CRIMSON LINE by BENDERCL"
    },
    "timestamp": fecha.isoformat()
}

requests.post(
    WEBHOOK,
    json={
        "content": "<@&1528804634293043290>",
        "embeds": [embed],
        "allowed_mentions": {
            "roles": ["1528804634293043290"]
        }
    }
)
