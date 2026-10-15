"""Limpieza, KPIs y visualizaciones del caso NorteSur Logística."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "raw" / "entregas_2024.csv"
OUTPUT = ROOT / "outputs"
OUTPUT.mkdir(exist_ok=True)

df = pd.read_csv(INPUT, parse_dates=["fecha_pedido"])
assert df["envio_id"].is_unique, "Hay IDs duplicados"
assert df.notna().all().all(), "Hay valores nulos"
df["mes"] = df["fecha_pedido"].dt.to_period("M").astype(str)
df["brecha_minutos"] = df["minutos_reales"] - df["sla_minutos"]

mensual = (df.groupby("mes", as_index=False)
    .agg(envios=("envio_id", "count"), pct_a_tiempo=("entregado_a_tiempo", "mean"),
         minutos_promedio=("minutos_reales", "mean"), reclamos_por_mil=("reclamo", "mean")))
mensual["pct_a_tiempo"] = (mensual["pct_a_tiempo"] * 100).round(1)
mensual["reclamos_por_mil"] = (mensual["reclamos_por_mil"] * 1000).round(1)
mensual.to_csv(OUTPUT / "kpis_mensuales.csv", index=False)

zona_franja = (df.groupby(["zona", "franja_horaria"], as_index=False)
    .agg(envios=("envio_id", "count"), pct_a_tiempo=("entregado_a_tiempo", "mean"),
         brecha_promedio_minutos=("brecha_minutos", "mean")))
zona_franja["pct_a_tiempo"] = (zona_franja["pct_a_tiempo"] * 100).round(1)
zona_franja.to_csv(OUTPUT / "desempeno_zona_franja.csv", index=False)

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(mensual["mes"], mensual["pct_a_tiempo"], marker="o", color="#15616D", linewidth=2.5)
ax.axhline(92, color="#E76F51", linestyle="--", label="Meta: 92%")
ax.set(title="Cumplimiento de entrega por mes", xlabel="Mes", ylabel="Entregas a tiempo (%)", ylim=(70, 100))
ax.tick_params(axis="x", rotation=45); ax.legend(); fig.tight_layout()
fig.savefig(OUTPUT / "cumplimiento_mensual.png", dpi=160); plt.close(fig)

pivote = df.pivot_table(index="zona", columns="franja_horaria", values="entregado_a_tiempo", aggfunc="mean").mul(100)
fig, ax = plt.subplots(figsize=(10, 5))
pivote.plot(kind="bar", ax=ax, color=["#83C5BE", "#006D77", "#E76F51"])
ax.set(title="Cumplimiento por zona y franja", xlabel="Zona", ylabel="Entregas a tiempo (%)", ylim=(55, 100))
ax.legend(title="Franja"); ax.tick_params(axis="x", rotation=25); fig.tight_layout()
fig.savefig(OUTPUT / "cumplimiento_zona_franja.png", dpi=160); plt.close(fig)

print("Análisis finalizado. Resultados disponibles en outputs/.")
