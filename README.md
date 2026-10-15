# Análisis de demoras en entregas de última milla

## Descripción del proyecto

Este proyecto presenta un caso de análisis de datos aplicado a una empresa ficticia de logística urbana llamada **NorteSur Logística**, con operaciones en Asunción y Gran Asunción.

El objetivo fue analizar el desempeño de las entregas realizadas durante 2024 e identificar los principales factores asociados a los retrasos.

> Nota: los datos utilizados son sintéticos y fueron creados únicamente con fines de portafolio. El caso, las métricas y el enfoque de análisis representan una situación de negocio realista.

---

## Situación de negocio

Durante el último trimestre de 2024, el área de Operaciones de NorteSur Logística observó un aumento en los reclamos de clientes por entregas demoradas.

La empresa contaba con información de cada envío, como zona de entrega, tipo de servicio, distancia, cantidad de pedidos por ruta, tráfico, lluvia, tiempo real de entrega y reclamos. Sin embargo, esos datos no estaban siendo utilizados para identificar dónde se originaban los incumplimientos.

La gerencia solicitó un análisis que permitiera responder:

- ¿Qué porcentaje de entregas llega dentro del tiempo prometido?
- ¿En qué zonas y horarios se concentran las demoras?
- ¿Qué condiciones operativas se relacionan con un peor cumplimiento?
- ¿Qué acciones podría tomar la empresa sin aumentar permanentemente su flota?

---

## Objetivo

Transformar datos operativos de entregas en información útil para que el equipo de Operaciones pueda priorizar mejoras en las rutas, horarios y asignación de repartidores.

---

## Datos analizados

El proyecto trabaja con una base sintética de **18.000 envíos** realizados entre enero y diciembre de 2024.

Principales variables disponibles:

- Identificador de envío
- Fecha del pedido
- Zona de entrega
- Tipo de servicio
- Franja horaria
- Kilómetros de ruta
- Cantidad de pedidos asignados por ruta
- Nivel de tráfico
- Condición de lluvia
- Tiempo real de entrega
- Tiempo prometido al cliente (SLA)
- Entrega a tiempo
- Reclamo del cliente

El detalle completo de las variables se encuentra en [`data/data_dictionary.md`](data/data_dictionary.md).

---

## Trabajo realizado

El análisis se desarrolló en las siguientes etapas:

1. Generación de una base de datos sintética y reproducible.
2. Validación de calidad de datos: valores nulos, duplicados y consistencia de métricas.
3. Creación de indicadores operativos.
4. Análisis de cumplimiento por mes, zona, franja horaria y tipo de servicio.
5. Identificación de factores asociados a las demoras.
6. Elaboración de recomendaciones para el equipo de Operaciones.

---

## Indicadores utilizados

- **Porcentaje de entregas a tiempo:** proporción de envíos entregados dentro del SLA prometido.
- **Tiempo promedio de entrega:** promedio de minutos desde el despacho hasta la entrega.
- **Brecha de entrega:** diferencia entre el tiempo real y el SLA.
- **Reclamos por cada 1.000 envíos:** indicador de impacto en experiencia del cliente.
- **Volumen de envíos:** cantidad de pedidos procesados por período, zona o servicio.

---

## Hallazgos principales

A partir del análisis se identificaron los siguientes patrones:

- La franja horaria de **17:00 a 20:00** presenta el menor nivel de cumplimiento.
- Las zonas de **San Lorenzo** y **Fernando de la Mora** concentran una mayor proporción de entregas fuera de plazo.
- El problema se intensifica en rutas con una carga alta de pedidos asignados.
- Los días de lluvia, especialmente cuando existe tráfico alto, aumentan el tiempo promedio de entrega y la probabilidad de reclamo.
- El servicio estándar concentra la mayor cantidad de incumplimientos debido a su mayor volumen operativo.

---

## Recomendaciones propuestas

| Prioridad | Recomendación | Objetivo |
|---|---|---|
| Alta | Reforzar la capacidad operativa entre las 17:00 y 20:00 en San Lorenzo y Fernando de la Mora. | Mejorar el cumplimiento en las zonas críticas. |
| Alta | Limitar la asignación de pedidos por ruta durante la franja pico. | Evitar sobrecarga de repartidores. |
| Media | Implementar una alerta operativa ante lluvia y tráfico alto. | Reasignar pedidos antes de que se acumulen demoras. |
| Media | Revisar el SLA prometido en rutas periféricas. | Alinear la expectativa del cliente con la capacidad real. |

