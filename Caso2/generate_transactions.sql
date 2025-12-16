-- Script para generar 10,000 transacciones sintéticas para la tabla "transacciones"

DO $$
DECLARE
    trans_count INTEGER := 10000;
    trx_date TIMESTAMP := NOW() - INTERVAL '2 years';
    trx_id TEXT;
    account_pool TEXT[] := ARRAY(SELECT 'ACC-' || LPAD(i::TEXT, 5, '0') FROM generate_series(1, 500) i);
    trx_type TEXT;
    trx_amount NUMERIC(15,2);
    trx_state TEXT;
    trx_channel TEXT;
    trx_description TEXT;
    trx_origin TEXT;
    trx_dest TEXT;
BEGIN
    FOR i IN 1..trans_count LOOP
        -- Generar ID de transacción
        trx_id := 'TRX-' || TO_CHAR(trx_date, 'YYYYMMDD') || '-' || LPAD(i::TEXT, 5, '0');

        -- Incrementar fecha para mantener orden cronológico
        trx_date := trx_date + INTERVAL '10 minutes';

        -- Seleccionar tipo de transacción con distribución
        trx_type := CASE
            WHEN random() < 0.4 THEN 'TRANSFERENCIA'
            WHEN random() < 0.65 THEN 'DEPOSITO'
            WHEN random() < 0.85 THEN 'RETIRO'
            ELSE 'PAGO_SERVICIO'
        END;

        -- Generar monto según tipo de transacción
        trx_amount := CASE trx_type
            WHEN 'TRANSFERENCIA' THEN round(random() * (5000000 - 10000) + 10000, 2)
            WHEN 'DEPOSITO' THEN round(random() * (10000000 - 20000) + 20000, 2)
            WHEN 'RETIRO' THEN round(random() * (3000000 - 10000) + 10000, 2)
            WHEN 'PAGO_SERVICIO' THEN round(random() * (500000 - 5000) + 5000, 2)
        END;

        -- Generar estado con distribución
        trx_state := CASE
            WHEN random() < 0.85 THEN 'EXITOSA'
            WHEN random() < 0.95 THEN 'PENDIENTE'
            ELSE 'RECHAZADA'
        END;

        -- Generar canal con distribución
        trx_channel := CASE
            WHEN random() < 0.5 THEN 'APP_MOVIL'
            WHEN random() < 0.8 THEN 'WEB'
            WHEN random() < 0.95 THEN 'CAJERO'
            ELSE 'SUCURSAL'
        END;

        -- Generar cuentas origen y destino
        trx_origin := account_pool[ceil(random() * array_length(account_pool, 1))];
        trx_dest := account_pool[ceil(random() * array_length(account_pool, 1))];

        -- Asegurar que las cuentas sean diferentes para transferencias
        IF trx_type = 'TRANSFERENCIA' THEN
            WHILE trx_dest = trx_origin LOOP
                trx_dest := account_pool[ceil(random() * array_length(account_pool, 1))];
            END LOOP;
        ELSE
            trx_dest := NULL; -- Sin cuenta destino para depósitos y retiros
        END IF;

        -- Generar descripción según tipo de transacción
        trx_description := CASE trx_type
            WHEN 'TRANSFERENCIA' THEN 'Transferencia a cuenta ' || trx_dest
            WHEN 'DEPOSITO' THEN 'Depósito en cuenta ' || trx_origin
            WHEN 'RETIRO' THEN 'Retiro de cuenta ' || trx_origin
            WHEN 'PAGO_SERVICIO' THEN 'Pago de servicio'
        END;

        -- Insertar transacción
        INSERT INTO transacciones (
            id_transaccion, fecha_hora, id_cuenta_origen, id_cuenta_destino,
            tipo_transaccion, monto, estado, canal, descripcion
        ) VALUES (
            trx_id, trx_date, trx_origin, trx_dest,
            trx_type, trx_amount, trx_state, trx_channel, trx_description
        );

        -- Limitar a 50 transacciones por cuenta por día
        IF i % 50 = 0 THEN
            trx_date := trx_date + INTERVAL '1 day';
        END IF;
    END LOOP;
END $$;