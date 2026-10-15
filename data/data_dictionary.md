# Diccionario de datos

| Campo | Tipo | Descripción |
|---|---|---|
| `envio_id` | texto | Identificador único del envío. |
| `fecha_pedido` | fecha | Fecha en que se registró el pedido. |
| `zona` | texto | Zona de entrega. |
| `servicio` | texto | Modalidad: Estándar, Express o Same Day. |
| `franja_horaria` | texto | Ventana comprometida para la entrega. |
| `km_ruta` | decimal | Distancia estimada de la ruta. |
| `pedidos_ruta` | entero | Pedidos asignados al repartidor en esa ruta. |
| `nivel_trafico` | texto | Bajo, Medio o Alto. |
| `lluvia` | booleano | Indicador de lluvia durante la entrega. |
| `minutos_reales` | entero | Duración real desde despacho hasta entrega. |
| `sla_minutos` | entero | Tiempo máximo prometido al cliente. |
| `entregado_a_tiempo` | booleano | Verdadero si `minutos_reales <= sla_minutos`. |
| `reclamo` | booleano | Si el cliente generó un reclamo asociado. |

## Controles de calidad aplicados

- `envio_id` único y sin valores nulos.
- Fechas dentro de 2024.
- Distancias y tiempos estrictamente positivos.
- Consistencia entre `entregado_a_tiempo`, `minutos_reales` y `sla_minutos`.
