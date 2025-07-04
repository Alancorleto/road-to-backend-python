from enum import Enum
import os
from dataclasses import dataclass
import json


class Prioridad(Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAJA = "baja"


@dataclass
class Tarea:
    nombre: str
    prioridad: Prioridad
    completada: bool = False

    def __str__(self):
        estado: str = "✓" if self.completada else "✗"
        return f"{self.nombre} {estado}"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "prioridad": self.prioridad.value,
            "completada": self.completada
        }



tareas_por_nombre: dict[str, Tarea] = {}
tareas_por_prioridad: dict[Prioridad, list[Tarea]] = {p: [] for p in Prioridad}


def agregar_tarea(nombre: str, prioridad_str: str) -> None:
    if nombre in tareas_por_nombre:
        print(f"La tarea '{nombre}' ya existe.")
        return

    if prioridad_str not in Prioridad._value2member_map_:
        print(f"Prioridad '{prioridad_str}' no válida. Debe ser 'alta', 'media' o 'baja'.")
        return

    prioridad_enum: Prioridad = Prioridad(prioridad_str)

    tarea = Tarea(nombre, prioridad_enum)
    tareas_por_nombre[nombre] = tarea
    tareas_por_prioridad[prioridad_enum].append(tarea)
    print(f"Tarea '{nombre}' agregada con prioridad '{prioridad_str}'.")


def imprimir_tareas() -> None:
    if not tareas_por_nombre:
        print("No hay tareas.")
    else:
        for prioridad in tareas_por_prioridad:
            print(f"\n[{prioridad.value.capitalize()}]")
            tareas: list[Tarea] = tareas_por_prioridad[prioridad]
            if not tareas:
                print("  No hay tareas.")
            else:
                for tarea in tareas_por_prioridad[prioridad]:
                    print(f"  {tarea}")
        print("")



def completar_tarea(nombre: str) -> None:
    if nombre not in tareas_por_nombre:
        print(f"La tarea '{nombre}' no existe.")
        return

    tarea = tareas_por_nombre[nombre]
    if tarea.completada:
        print(f"La tarea '{nombre}' ya está completada.")
    else:
        tarea.completada = True
        print(f"Tarea '{nombre}' marcada como completada.")


def eliminar_tarea(nombre: str) -> None:
    if nombre not in tareas_por_nombre:
        print(f"La tarea '{nombre}' no existe.")
        return

    tarea = tareas_por_nombre[nombre]
    tareas_por_prioridad[tarea.prioridad].remove(tarea)
    del tareas_por_nombre[nombre]
    print(f"Tarea '{nombre}' eliminada.")


def limpiar_pantalla() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def guardar_tareas() -> None:
    with open("tareas.json", "w") as archivo:
        json.dump([tarea.to_dict() for tarea in tareas_por_nombre.values()], archivo, indent=4)


def cargar_tareas() -> None:
    global tareas_por_nombre, tareas_por_prioridad
    try:
        with open("tareas.json", "r") as archivo:
            tareas_data = json.load(archivo)
            for tarea_data in tareas_data:
                tarea = Tarea(tarea_data["nombre"], Prioridad(tarea_data["prioridad"]), tarea_data["completada"])
                tareas_por_nombre[tarea.nombre] = tarea
                tareas_por_prioridad[tarea.prioridad].append(tarea)
    except FileNotFoundError:
        print("No se encontraron tareas guardadas.")
    except json.JSONDecodeError:
        print("Error al leer el archivo de tareas. Asegúrese de que el formato sea correcto.")


def main() -> None:
    if os.path.exists("tareas.json"):
        cargar_tareas()
    
    while True:
        print("\nLista de Tareas")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion: str = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre: str = input("Ingrese el nombre de la tarea: ")
            prioridad: str = input("Ingrese la prioridad (alta, media, baja): ")
            agregar_tarea(nombre, prioridad)
        elif opcion == "2":
            imprimir_tareas()
        elif opcion == "3":
            nombre: str = input("Ingrese el nombre de la tarea a completar: ")
            completar_tarea(nombre)
        elif opcion == "4":
            nombre: str = input("Ingrese el nombre de la tarea a eliminar: ")
            eliminar_tarea(nombre)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        guardar_tareas()
        input("Presione Enter para continuar...")
        limpiar_pantalla()


if __name__ == "__main__":
    main()
