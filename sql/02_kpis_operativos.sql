-- Evolución mensual de los principales indicadores
SELECT
    DATE_TRUNC('month', fecha_pedido)::date AS mes,
    COUNT(*) AS envios,
    ROUND(100.0 * AVG(entregado_a_tiempo::int), 1) AS pct_a_tiempo,
    ROUND(AVG(minutos_reales), 1) AS minutos_promedio,
    ROUND(1000.0 * AVG(reclamo::int), 1) AS reclamos_por_mil
FROM entregas
GROUP BY 1
ORDER BY 1;

-- Desempeño por zona y franja
SELECT
    zona,
    franja_horaria,
    COUNT(*) AS envios,
    ROUND(100.0 * AVG(entregado_a_tiempo::int), 1) AS pct_a_tiempo,
    ROUND(AVG(minutos_reales - sla_minutos), 1) AS brecha_promedio_minutos
FROM entregas
GROUP BY 1, 2
HAVING COUNT(*) >= 50
ORDER BY pct_a_tiempo, envios DESC;
