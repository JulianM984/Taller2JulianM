# Resultados de los Casos de Prueba

Este archivo contiene los resultados de los 15 casos de prueba ejecutados para la API del Bureau de Crédito.

| **ID** | **Escenario**                              | **Resultado**                                                                                     |
|--------|-------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1      | Consulta exitosa (path feliz)             | ✅ Éxito: Retorna historial crediticio con datos completos y sin alertas                          |
| 2      | Cliente con deudas activas               | ✅ Éxito: Retorna historial con detalle de deudas activas                                         |
| 3      | Cliente en lista de riesgo CIFIN         | ✅ Éxito: Retorna alerta de riesgo con detalles                                                  |
| 4      | Documento de identidad inválido          | ✅ Éxito: Retorna error 404 con mensaje "Cliente no encontrado"                                  |
| 5      | Formato de documento incorrecto          | ✅ Éxito: Retorna error 400 con mensaje "Formato de documento inválido"                          |
| 6      | Servicio caído                           | ✅ Éxito: Retorna error 503 con mensaje "Servicio no disponible"                                 |
| 7      | Timeout en la respuesta                  | ✅ Éxito: Retorna error 504 con mensaje "Tiempo de espera agotado"                               |
| 8      | Respuesta inválida del API               | ✅ Éxito: Retorna error 500 con mensaje "Respuesta inválida del servicio"                        |
| 9      | Documento duplicado                      | ✅ Éxito: Retorna error 409 con mensaje "Documento duplicado"                                    |
| 10     | Cliente extranjero                       | ✅ Éxito: Retorna mensaje "Cliente extranjero, no aplica para consulta"                          |
| 11     | Cliente sin historial crediticio         | ✅ Éxito: Retorna mensaje "Sin historial crediticio"                                             |
| 12     | Consulta con documento nulo              | ✅ Éxito: Retorna error 400 con mensaje "Documento requerido"                                    |
| 13     | Consulta con caracteres especiales       | ✅ Éxito: Retorna error 400 con mensaje "Formato de documento inválido"                          |
| 14     | Consulta con cliente fallecido           | ✅ Éxito: Retorna mensaje "Cliente fallecido, no aplica para consulta"                           |
| 15     | Consulta con cliente menor de edad       | ✅ Éxito: Retorna mensaje "Cliente menor de edad, no aplica para consulta"                       |

**Leyenda:**
- ✅ Éxito: El caso de prueba pasó satisfactoriamente.
- ❌ Fallo: El caso de prueba no cumplió con el resultado esperado.
