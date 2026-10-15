# Informe ejecutivo

## Situación

El indicador de entregas a tiempo cerró diciembre en 86%, por debajo de la meta operativa de 92%. La dirección solicitó un diagnóstico para decidir dónde reasignar capacidad durante el próximo trimestre.

## Hallazgos

1. **El problema se intensifica al final de la jornada.** La franja 17:00–20:00 presenta el menor cumplimiento. El efecto es mayor en rutas con más de 13 pedidos asignados.
2. **Hay concentración geográfica.** San Lorenzo y Fernando de la Mora combinan distancia media más alta, tráfico intenso y mayor volumen de pedidos.
3. **El servicio estándar absorbe el impacto.** Al tener mayor volumen y menor holgura frente al tráfico, concentra la mayor cantidad absoluta de incumplimientos.
4. **La lluvia amplifica una operación ya exigida.** En rutas con tráfico alto, los días de lluvia elevan el tiempo medio y los reclamos.

## Recomendaciones priorizadas

| Prioridad | Acción | Responsable sugerido | Métrica de seguimiento |
|---|---|---|---|
| Alta | Reforzar 17:00–20:00 en San Lorenzo y Fernando de la Mora con capacidad flexible. | Operaciones | % a tiempo por zona y franja |
| Alta | Limitar a 12 pedidos por ruta en la franja pico para estándar. | Planificación | Pedidos por ruta / cumplimiento |
| Media | Activar aviso preventivo y redistribución ante lluvia + tráfico alto. | Customer Experience | Reclamos por 1.000 envíos |
| Media | Revisar la promesa de servicio en rutas periféricas. | Producto | Brecha entre SLA y tiempo real |

## Impacto esperado

La estimación no supone crecimiento de flota permanente: reasigna capacidad donde el costo de demora es mayor. Si se recupera el cumplimiento de las dos zonas críticas hasta el promedio general y se reduce la sobrecarga de rutas, el indicador global podría mejorar entre 4 y 6 puntos porcentuales.

## Limitaciones

Se trata de un dataset sintético y observacional. Para una implementación real, validaría disponibilidad de repartidores, costo por turno, dirección exacta, hora de despacho y causa codificada de cada incidencia antes de atribuir causalidad.
