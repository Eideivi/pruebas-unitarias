# Proyecto: Calculadora de Impuestos sobre Ventas

## Descripción
Este proyecto implementa una calculadora de impuestos sobre ventas que permite calcular el total de una compra considerando:
- Un descuento opcional sobre el precio del producto.
- El impuesto aplicable basado en una tasa establecida.
- Tarifas adicionales que se suman al total final.

Además, se han desarrollado pruebas unitarias utilizando `pytest` para garantizar la correcta funcionalidad de los cálculos.

---

## Casos de Uso
Este sistema cubre los siguientes casos de uso:

1. Cálculo del total de una compra con impuesto y descuentos.
   - Se ingresa un precio base y un descuento opcional.
   - Se aplica el impuesto correspondiente al subtotal.
   - Se suman tarifas adicionales si existen.

2. Validación de datos inválidos.
   - Si se ingresa un precio negativo, el sistema genera un error.
   - Si el descuento es mayor que el precio, el sistema lo rechaza.
   - Si se ingresan valores inválidos, se levanta una excepción adecuada.

---

## Pruebas Unitarias Implementadas
Se han desarrollado pruebas unitarias utilizando `pytest`, cubriendo diferentes caminos y condiciones posibles.

### test_calculate_tax()
**Objetivo:** Verificar que el cálculo del impuesto es correcto en diferentes casos.  
**Casos cubiertos:**
   - Cálculo de impuesto sobre diferentes precios y descuentos.
   - Valores borde para asegurar precisión en el cálculo.

### test_calculate_total()
**Objetivo:** Garantizar que el total se calcule correctamente con impuestos y tarifas adicionales.  
**Casos cubiertos:**
   - Diferentes combinaciones de precios, descuentos e impuestos.
   - Manejo de tarifas adicionales.

### test_invalid_values()
**Objetivo:** Asegurar que la aplicación maneja correctamente los valores inválidos.  
**Casos cubiertos:**
   - Precios negativos.
   - Descuentos mayores que el precio.
   - Otros valores que deberían ser rechazados.

### test_breakdown()
**Objetivo:** Validar que el desglose de cálculo (`breakdown()`) devuelve los valores correctos.  
**Casos cubiertos:**
   - Verificación de cada campo del desglose (precio, descuento, impuesto, tarifas, total).

---

## Cómo Ejecutar las Pruebas

### 1. Clonar el Repositorio
Si aún no tienes el repositorio, clónalo desde GitHub con:
```bash
git clone https://github.com/tu-usuario/pruebas-unitarias.git
cd pruebas-unitarias
```

### 2. Instalar Dependencias
Asegúrate de tener `pytest` instalado. Si no lo tienes, instálalo con:
```bash
pip install pytest
```

### 3. Ejecutar las Pruebas
Para correr todas las pruebas unitarias, usa:
```bash
python -m pytest -v
```

Si quieres ejecutar solo un archivo de prueba específico:
```bash
python -m pytest test_sales_tax_updated.py -v
```

---

Este documento describe los pasos necesarios para ejecutar y validar el correcto funcionamiento del proyecto.
