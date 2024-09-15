def convertir_pesos_a_dolares(pesos, tasa_cambio):
    return pesos / tasa_cambio

def convertir_dolares_a_pesos(dolares, tasa_cambio):
    return dolares * tasa_cambio

def main():
    print("Programa de conversión de monedas")
    print("1. Pesos a Dólares")
    print("2. Dólares a Pesos")
    
    opcion = input("Selecciona una opción (1 o 2): ")
    
    if opcion not in ['1', '2']:
        print("Opción no válida.")
        return
    
    tasa_cambio = float(input("Introduce la tasa de cambio (por ejemplo, 20 para 1 dólar = 20 pesos): "))
    
    if opcion == '1':
        pesos = float(input("Introduce la cantidad en pesos: "))
        dolares = convertir_pesos_a_dolares(pesos, tasa_cambio)
        print(f"{pesos} pesos son {dolares:.2f} dólares.")
    
    elif opcion == '2':
        dolares = float(input("Introduce la cantidad en dólares: "))
        pesos = convertir_dolares_a_pesos(dolares, tasa_cambio)
        print(f"{dolares} dólares son {pesos:.2f} pesos.")

if __name__ == "__main__":
    main()
