def verificar_edad_y_licencia(edad, tiene_licencia):
    if edad >= 18:
        if tiene_licencia:
            return "Puedes conducir."
        else:
            return "Eres mayor de edad pero no tienes licencia. No puedes conducir."
    else:
        return "Eres menor de edad. No puedes conducir."

def main():
    try:
        edad = int(input("Introduce tu edad: "))
        licencia_input = input("¿Tienes licencia de conducir? ").strip().lower()
        
        if licencia_input == 'sí' or licencia_input == 'si':
            tiene_licencia = True
        elif licencia_input == 'no':
            tiene_licencia = False
        else:
            print("Respuesta inválida para la licencia de conducir.")
            return

        resultado = verificar_edad_y_licencia(edad, tiene_licencia)
        print(resultado)
        
    except ValueError:
        print("No puedes conducir.")

if __name__ == "__main__":
    main()

