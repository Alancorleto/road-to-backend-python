from datetime import date


# Diccionario que mapea números de meses a sus nombres en español
meses_por_numero: dict[int, str] = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}


# Función que saluda al usuario con su nombre, edad y ciudad
def saludar_usuario(nombre: str, edad: int, ciudad: str) -> None:
    hoy: date = date.today()
    dia: int = hoy.day
    mes: int = hoy.month
    mes_palabra: str = meses_por_numero[mes]
    anio: int = hoy.year

    # Printea el saludo con los datos del usuario
    print(f"Hola {nombre}, tenés {edad} años y vivís en {ciudad}.")

    if edad < 18:
        print("Sos menor de edad.")

    print(f"Hoy es {dia} de {mes_palabra} de {anio}. ¡Que tengas un buen día!")


def pedir_nombre() -> str:
    nombre: str = ""
    while True:
        nombre = input("¿Cuál es tu nombre? ")
        if nombre.strip():  # Verifica que no esté vacío
            return nombre
        else:
            print("Por favor, ingresa un nombre válido.")


def pedir_edad() -> int:
    edad: int = 0
    while True:
        try: 
            edad = int(input("¿Cuál es tu edad? "))
            if edad >= 0:
                return edad
            else:
                print("Por favor, ingresa una edad válida (número positivo).")
        except ValueError:
            print("Por favor, ingresa un número válido para la edad (solo dígitos).")


def pedir_ciudad() -> str:
    ciudad: str = ""
    while True:
        ciudad = input("¿Cuál es tu ciudad? ")
        if ciudad.strip():  # Verifica que no esté vacío
            return ciudad
        else:
            print("Por favor, ingresa un nombre de ciudad válido.")


def main() -> None:
    print("¡Bienvenido al programa de saludo!")
    nombre: str = pedir_nombre()
    edad: int = pedir_edad()
    ciudad: str = pedir_ciudad()
    saludar_usuario(nombre, edad, ciudad)


if __name__ == "__main__":
    main()