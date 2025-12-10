def aplicar_descuento(precio, porcentaje):
    """
    Aplica un descuento al precio.
    """
    if precio < 0 or porcentaje < 0:
        raise ValueError("Precio y porcentaje deben ser positivos")

    descuento = precio * (porcentaje / 100)
    return round(precio - descuento, 2)


# Ejemplo de ejecución local
if __name__ == "__main__":
    precio_final = aplicar_descuento(100, 15)
    print(f"Precio final con descuento: ${precio_final}")
