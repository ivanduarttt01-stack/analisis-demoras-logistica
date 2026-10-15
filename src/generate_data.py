"""Genera datos sintéticos reproducibles para el caso de portafolio."""
from pathlib import Path
import random
import csv
from datetime import date, timedelta

random.seed(2024)
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "entregas_2024.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

zonas = {
    "Asunción": (5.5, 0.31), "Luque": (10.0, 0.20), "San Lorenzo": (12.5, 0.16),
    "Fernando de la Mora": (9.0, 0.13), "Lambaré": (7.0, 0.11), "Mariano Roque Alonso": (11.0, 0.09),
}
franjas = [("09:00-12:00", 0.28, 0), ("13:00-16:00", 0.34, 4), ("17:00-20:00", 0.38, 14)]
servicios = [("Estándar", 0.62, 100), ("Express", 0.27, 70), ("Same Day", 0.11, 150)]
inicio = date(2024, 1, 1)

with OUT.open("w", newline="", encoding="utf-8") as f:
    campos = ["envio_id", "fecha_pedido", "zona", "servicio", "franja_horaria", "km_ruta", "pedidos_ruta", "nivel_trafico", "lluvia", "minutos_reales", "sla_minutos", "entregado_a_tiempo", "reclamo"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    for i in range(1, 18001):
        fecha = inicio + timedelta(days=random.randrange(366))
        zona = random.choices(list(zonas), weights=[x[1] for x in zonas.values()])[0]
        km_base = zonas[zona][0]
        franja, _, penalidad_franja = random.choices(franjas, weights=[x[1] for x in franjas])[0]
        servicio, _, sla = random.choices(servicios, weights=[x[1] for x in servicios])[0]
        trafico = random.choices(["Bajo", "Medio", "Alto"], weights=[0.18, 0.47, 0.35 if franja == "17:00-20:00" else 0.22])[0]
        lluvia = random.random() < (0.30 if fecha.month in [10, 11, 12, 1, 2, 3] else 0.16)
        pedidos = max(4, int(random.gauss(10 + (3 if franja == "17:00-20:00" else 0), 2.5)))
        km = round(max(1.2, random.gauss(km_base, 2.3)), 1)
        trafico_min = {"Bajo": 0, "Medio": 10, "Alto": 23}[trafico]
        zona_penalidad = 8 if zona in ["San Lorenzo", "Fernando de la Mora"] else 0
        tiempo = round(max(22, 18 + km * 4.1 + pedidos * 2.3 + trafico_min + penalidad_franja + zona_penalidad + (13 if lluvia else 0) + random.gauss(0, 10)))
        a_tiempo = tiempo <= sla
        reclamo = (not a_tiempo and random.random() < 0.24) or (a_tiempo and random.random() < 0.008)
        writer.writerow({"envio_id": f"NS-{i:05d}", "fecha_pedido": fecha.isoformat(), "zona": zona, "servicio": servicio, "franja_horaria": franja, "km_ruta": km, "pedidos_ruta": pedidos, "nivel_trafico": trafico, "lluvia": lluvia, "minutos_reales": tiempo, "sla_minutos": sla, "entregado_a_tiempo": a_tiempo, "reclamo": reclamo})

print(f"Archivo creado: {OUT} (18.000 envíos)")
