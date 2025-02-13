import pytest
from sales_tax_calculator import SalesTaxCalculator

@pytest.fixture
def calculator():
    return SalesTaxCalculator(0.15, additional_fees=5.0)  # 15% de impuesto + $5 de tarifa adicional

# Prueba de cálculo de impuesto
@pytest.mark.parametrize("price, discount, expected_tax", [
    (100, 0, 15.0),
    (100, 10, 13.5),
    (50, 5, 6.75),
    (200, 20, 27.0)
])
def test_calculate_tax(calculator, price, discount, expected_tax):
    assert calculator.calculate_tax(price, discount) == expected_tax

# Prueba de cálculo total con tarifas adicionales
@pytest.mark.parametrize("price, discount, expected_total", [
    (100, 0, 120.0),  # 100 + 15% impuesto + $5 tarifa adicional
    (100, 10, 108.5),
    (50, 5, 56.75),  # Se cambia el valor esperado para coincidir con la lógica actual
    (200, 20, 212.0)
])
def test_calculate_total(calculator, price, discount, expected_total):
    assert calculator.calculate_total(price, discount) == expected_total

# Prueba de valores inválidos
@pytest.mark.parametrize("price, discount", [
    (-10, 0),
    (100, -5),
    (50, 60)
])
def test_invalid_values(calculator, price, discount):
    with pytest.raises(ValueError):
        calculator.calculate_total(price, discount)

# Prueba de desglose con tarifas adicionales
def test_breakdown(calculator):
    breakdown = calculator.breakdown(100, 10)
    expected = {
        "Precio original": 100.0,
        "Descuento": 10.0,
        "Precio con descuento": 90.0,
        "Impuesto": 13.5,
        "Tarifas adicionales": 5.0,
        "Total con impuesto y tarifas": 108.5
    }
    assert breakdown == expected
