CREATE TABLE entregas (
    envio_id VARCHAR(20) PRIMARY KEY,
    fecha_pedido DATE NOT NULL,
    zona VARCHAR(50) NOT NULL,
    servicio VARCHAR(20) NOT NULL,
    franja_horaria VARCHAR(20) NOT NULL,
    km_ruta NUMERIC(6,2) CHECK (km_ruta > 0),
    pedidos_ruta INTEGER CHECK (pedidos_ruta > 0),
    nivel_trafico VARCHAR(10) NOT NULL,
    lluvia BOOLEAN NOT NULL,
    minutos_reales INTEGER CHECK (minutos_reales > 0),
    sla_minutos INTEGER CHECK (sla_minutos > 0),
    entregado_a_tiempo BOOLEAN NOT NULL,
    reclamo BOOLEAN NOT NULL
);

-- PostgreSQL: \copy entregas FROM 'data/raw/entregas_2024.csv' CSV HEADER;
