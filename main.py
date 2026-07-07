import random
import requests
import os
from datetime import datetime
from zoneinfo import ZoneInfo

WEBHOOK = os.getenv("WEBHOOK")

# ID del rol que deseas mencionar
ROLE_ID = "123456789012345678"

# Hora de Chile
fecha = datetime.now(ZoneInfo("America/Santiago"))

# Frecuencia aleatoria
frecuencia = round(random.uniform(200.00, 999.99), 2)

embed = {
    "title": "📻 Frecuencia del Día",
    "description": "La frecuencia asignada para las comunicaciones de hoy es:",
    "color": 3447003,
    "fields": [
        {
            "name": "📡 Frecuencia",
            "value": f"**{frecuencia:.2f} MHz**",
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
        "content": f"<@&{1497107907429273661}>",
        "embeds": [embed],
        "allowed_mentions": {
            "roles": [1497107907429273661]
        }
    }
)
