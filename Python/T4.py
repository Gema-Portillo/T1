def calcular_descuento(total_compra):
    if total_compra >= 1000:
        descuento = 0.10  # 10% de descuento
    elif total_compra >= 500:
        descuento = 0.05  # 5% de descuento
    else:
        descuento = 0.00  # Sin descuento
    
    return descuento

def aplicar_descuento_adicional(total_compra, descuento, es_vip):
    total_con_descuento = total_compra * (1 - descuento)
    if es_vip:
        descuento_adicional = 0.05  # 5% adicional para VIP
        total_con_descuento *= (1 - descuento_adicional)
    
    return total_con_descuento

def main():
    # Solicitar el monto total de la compra
    total_compra = float(input("Introduce el monto total de la compra: $"))
    
    # Preguntar si el cliente es VIP
    es_vip = input("¿Eres miembro VIP? (sí/no): ").strip().lower() == "sí"
    
    # Calcular el descuento basado en el monto de la compra
    descuento = calcular_descuento(total_compra)
    
    # Aplicar el descuento adicional si el cliente es VIP
    total_final = aplicar_descuento_adicional(total_compra, descuento, es_vip)
    
    # Mostrar el total final a pagar
    print(f"El TOTAL FINAL A PAGAR es: ${total_final:.2f}")

if __name__ == "__main__":
    main()
