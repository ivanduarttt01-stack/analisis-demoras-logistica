# Caso de estudio: reducción de demoras en última milla

**Rol simulado:** Analista de Datos | **Industria:** logística urbana | **Periodo analizado:** enero a diciembre de 2024

## Contexto

NorteSur Logística es una empresa ficticia de entregas urbanas que opera en Asunción y Gran Asunción. Durante el último trimestre de 2024, la gerencia detectó un aumento en los reclamos por entregas fuera de plazo, pero no contaba con una vista única para entender qué zonas, franjas horarias o tipos de servicio explicaban el problema.

El objetivo de este proyecto fue convertir datos operativos de 18.000 envíos en recomendaciones accionables para mejorar el cumplimiento de la promesa de entrega sin aumentar la flota.

> Los datos fueron generados de forma sintética exclusivamente para fines de portafolio. Las reglas de negocio, métricas y conclusiones reproducen un caso de análisis realista.

## Preguntas de negocio

1. ¿Cómo evolucionó el porcentaje de entregas a tiempo durante 2024?
2. ¿Qué zonas, franjas horarias y servicios concentran más incumplimientos?
3. ¿Qué variables operativas se relacionan con las demoras?
4. ¿Qué acciones priorizar en el siguiente trimestre?

## Resultado ejecutivo

El análisis identifica que el deterioro del cumplimiento se concentra en la franja de **17:00 a 20:00**, especialmente en **San Lorenzo y Fernando de la Mora**, y afecta de forma desproporcionada a los envíos estándar. Los principales impulsores son el volumen por repartidor, la lluvia y las rutas de alta congestión.

La recomendación es reasignar capacidad en el pico vespertino, establecer un corte operativo para servicios estándar y activar un protocolo de contingencia climática. En el escenario conservador, estas medidas recuperan entre **4 y 6 puntos porcentuales** de cumplimiento en las zonas críticas.

## Herramientas

- **SQL (PostgreSQL):** modelado, limpieza y consultas de KPI.
- **Python:** `pandas` y `matplotlib` para análisis y visualización.
- **Git/GitHub:** versionado y documentación reproducible.

## Estructura

```text
.
├── data/
│   ├── raw/                 # Se genera aquí la base sintética
│   └── data_dictionary.md
├── docs/
│   └── caso_negocio.md      # Hallazgos y recomendaciones
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_kpis_operativos.sql
│   └── 03_analisis_demoras.sql
├── src/
│   ├── generate_data.py     # Genera 18.000 envíos reproducibles
│   └── analysis.py          # Ejecuta limpieza, KPIs y gráficos
├── outputs/                 # Archivos creados por el análisis
├── requirements.txt
└── README.md
```

## Cómo reproducirlo

```bash
python -m venv .venv
.venv\\Scripts\\activate       # Windows
pip install -r requirements.txt
python src/generate_data.py
python src/analysis.py
```

Al terminar encontrarás las tablas y gráficos en `outputs/`.

## Publicación en GitHub

1. Creá un repositorio nuevo con el nombre `analisis-demoras-logistica`.
2. Subí el contenido de esta carpeta (no la carpeta contenedora) al repositorio.
3. Ejecutá los dos scripts antes de publicar si querés versionar también las tablas y gráficos generados; quitá las dos reglas `outputs/*.csv` y `outputs/*.png` de `.gitignore` en ese caso.
4. Usá como descripción: `Caso de estudio con SQL y Python sobre entregas urbanas y cumplimiento de SLA.`

Sugerencia de nombre del repositorio: `analisis-demoras-logistica`.

## Competencias demostradas

- Traducción de una necesidad operativa en preguntas medibles.
- Preparación y validación de datos.
- Definición de métricas: cumplimiento, demora promedio, volumen y reclamos.
- Segmentación por zona, servicio y franja horaria.
- Comunicación de recomendaciones con impacto esperado.

## Cómo incluirlo en el CV

**Proyecto de portafolio — Analista de Datos, NorteSur Logística (caso simulado)**  
Analicé 18.000 entregas urbanas con SQL y Python para identificar factores asociados a demoras. Detecté zonas y franjas críticas, propuse una reasignación de capacidad y un protocolo climático con potencial de recuperar 4–6 pp de cumplimiento de entrega.

