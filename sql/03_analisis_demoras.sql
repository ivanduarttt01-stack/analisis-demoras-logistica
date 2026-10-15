-- Factores operativos asociados a incumplimientos
SELECT
    nivel_trafico,
    lluvia,
    CASE
        WHEN pedidos_ruta <= 8 THEN 'Hasta 8'
        WHEN pedidos_ruta <= 12 THEN '9 a 12'
        ELSE '13 o más'
    END AS carga_ruta,
    COUNT(*) AS envios,
    ROUND(100.0 * AVG(entregado_a_tiempo::int), 1) AS pct_a_tiempo,
    ROUND(100.0 * AVG(reclamo::int), 1) AS pct_reclamo
FROM entregas
GROUP BY 1, 2, 3
ORDER BY pct_a_tiempo;
