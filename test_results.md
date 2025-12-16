# Resultados de los Casos de Prueba Automatizados

## Resumen
- Total de pruebas ejecutadas: 15
- Total de pruebas exitosas: 0
- Total de fallos: 15

## Detalles de los Fallos

### Caso: `test_concurrencia_transferencias`
- **Error:** `404 not found in [200, 400]`
- **Línea:** 116

### Caso: `test_cuenta_bloqueada`
- **Error:** `404 != 400`
- **Línea:** 126

### Caso: `test_cuenta_destino_invalida`
- **Error:** `404 != 400`
- **Línea:** 76

### Caso: `test_cuenta_origen_igual_destino`
- **Error:** `404 != 400`
- **Línea:** 136

### Caso: `test_exceder_limite_diario`
- **Error:** `404 != 400`
- **Línea:** 25

### Caso: `test_exceder_limite_mensual`
- **Error:** `404 != 400`
- **Línea:** 35

### Caso: `test_horario_mantenimiento`
- **Error:** `404 != 503`
- **Línea:** 66

### Caso: `test_saldo_insuficiente`
- **Error:** `404 != 400`
- **Línea:** 45

### Caso: `test_token_otp_invalido`
- **Error:** `404 != 400`
- **Línea:** 56

### Caso: `test_transferencia_decimales_excesivos`
- **Error:** `404 != 400`
- **Línea:** 105

### Caso: `test_transferencia_exitosa`
- **Error:** `404 != 200`
- **Línea:** 15

### Caso: `test_transferencia_limite_diario`
- **Error:** `404 != 200`
- **Línea:** 146

### Caso: `test_transferencia_limite_mensual`
- **Error:** `404 != 200`
- **Línea:** 156

### Caso: `test_transferencia_monto_minimo`
- **Error:** `404 not found in [200, 400]`
- **Línea:** 86

### Caso: `test_transferencia_monto_negativo`
- **Error:** `404 != 400`
- **Línea:** 95

## Conclusión
Todos los casos de prueba fallaron debido a que el servidor respondió con un código de estado `404` (no encontrado). Esto indica que las rutas de la API pueden no estar configuradas correctamente o que el servidor no está respondiendo como se esperaba. Es necesario revisar la configuración del servidor y las rutas expuestas.