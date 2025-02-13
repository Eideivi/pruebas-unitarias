class SalesTaxCalculator:
    def __init__(self, tax_rate: float, additional_fees: float = 0):
        """Inicializa la calculadora con una tasa de impuesto y tarifas adicionales opcionales."""
        if tax_rate < 0 or tax_rate > 1:
            raise ValueError("La tasa de impuesto debe estar entre 0 y 1.")
        if additional_fees < 0:
            raise ValueError("Las tarifas adicionales no pueden ser negativas.")
        self.tax_rate = tax_rate
        self.additional_fees = additional_fees

    def calculate_total(self, price: float, discount: float = 0) -> float:
        """Calcula el precio total con impuesto y tarifas adicionales incluidos, aplicando un descuento opcional."""
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        if discount < 0 or discount > price:
            raise ValueError("El descuento debe estar entre 0 y el precio del producto.")
        
        discounted_price = price - discount  # Aplicar descuento
        total_tax = discounted_price * self.tax_rate  # Calcular impuesto sobre el precio con descuento
        total_price = discounted_price + total_tax + self.additional_fees  # Sumar impuesto y tarifas adicionales
        return round(total_price, 2)  # Redondear el resultado final

    def calculate_tax(self, price: float, discount: float = 0) -> float:
        """Calcula solo el monto del impuesto, considerando el descuento."""
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        if discount < 0 or discount > price:
            raise ValueError("El descuento debe estar entre 0 y el precio del producto.")
        discounted_price = price - discount
        return round(discounted_price * self.tax_rate, 2)

    def breakdown(self, price: float, discount: float = 0) -> dict:
        """Devuelve un desglose detallado del cálculo del precio, impuesto, tarifas adicionales y total."""
        discounted_price = price - discount
        total_tax = self.calculate_tax(price, discount)
        total_price = discounted_price + total_tax + self.additional_fees
        return {
            "Precio original": round(price, 2),
            "Descuento": round(discount, 2),
            "Precio con descuento": round(discounted_price, 2),
            "Impuesto": round(total_tax, 2),
            "Tarifas adicionales": round(self.additional_fees, 2),
            "Total con impuesto y tarifas": round(total_price, 2)
        }


# Ejemplo de uso
if __name__ == "__main__":
    calculator = SalesTaxCalculator(0.15, additional_fees=5.0)  # 15% de impuesto + $5 de tarifa adicional
    price = 100.0
    discount = 10.0
    print(calculator.breakdown(price, discount))
