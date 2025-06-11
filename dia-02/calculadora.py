import sys


def main() -> None:
    while True:
        imprimir_menu()

        opcion: int = pedir_opcion()

        operacion = opciones_menu[opcion][1]
        
        operacion()

        input("Presione Enter para continuar...")


def imprimir_menu() -> None:
    print("--- CALCULADORA ---")
    for num in opciones_menu:
        print(f"{num}. {opciones_menu[num][0]}")


def pedir_opcion() -> int:
    opcion : int = -1
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if opcion < 1 or opcion > 5:
                print("Error: Debe ingresar un número entre 1 y 5.")
            else:
                return opcion
        except ValueError:
            print("Error: Debe ingresar un número entero entre 1 y 5.")


def sumar() -> float:
    num1: float = pedir_numero("Ingrese el primer número: ")
    num2: float = pedir_numero("Ingrese el segundo número: ")
    print(f"Resultado: {num1 + num2}")


def restar() -> float:
    num1: float = pedir_numero("Ingrese el primer número: ")
    num2: float = pedir_numero("Ingrese el segundo número: ")
    print(f"Resultado: {num1 - num2}")


def multiplicar() -> float:
    num1: float = pedir_numero("Ingrese el primer número: ")
    num2: float = pedir_numero("Ingrese el segundo número: ")
    print(f"Resultado: {num1 * num2}")


def dividir() -> float:
    num1: float = pedir_numero("Ingrese el primer número: ")
    num2: float = 0.0
    while True:
        num2 = pedir_numero("Ingrese el segundo número: ")
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            break
    print(f"Resultado: {num1 / num2}")


def salir() -> None:
    print("Saliendo de la calculadora. ¡Hasta luego!")
    sys.exit(0)


def pedir_numero(mensaje: str) -> float:
    while True:
        try:
            numero: float = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")


opciones_menu: dict[int, (str, callable)] = {
    1: ("Sumar", sumar),
    2: ("Restar", restar),
    3: ("Multiplicar", multiplicar),
    4: ("Dividir", dividir),
    5: ("Salir", salir),
}


if __name__ == "__main__":
    main()
