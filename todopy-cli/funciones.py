"""
funciones.py — Lógica del gestor de tareas (ToDoPy)

Descripción
-----------
Módulo con operaciones de tareas (añadir, ver, completar, eliminar)
y persistencia simple en JSON.

"""

import json
import os

ARCHIVO = "tareas.json"

# Estado en memoria
tareas = []  # list[dict[str, Any]]


def cargar_tareas() -> None:
    """Carga tareas desde el archivo JSON si existe.
    Si el archivo no existe o está corrupto, inicializa una lista vacía.
    """
    global tareas
    if not os.path.exists(ARCHIVO):
        tareas = []
        return

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            tareas = data
        else:
            tareas = []
            print("⚠ El archivo de tareas no tiene el formato esperado. Se iniciará vacío.")
    except json.JSONDecodeError:
        tareas = []
        print("⚠ No se pudieron leer las tareas (JSON inválido). Se iniciará vacío.")
    except OSError as e:
        tareas = []
        print(f"⚠ Error de lectura de '{ARCHIVO}': {e}. Se iniciará vacío.")


def guardar_tareas() -> None:
    """Guarda la lista `tareas` en el archivo JSON con indentación legible."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(tareas, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"⚠ No se pudo guardar en '{ARCHIVO}': {e}")


def mostrar_menu() -> None:
    """Imprime el menú principal en consola."""
    print("═" * 42)
    print("      ToDoPy — Gestor de Tareas")
    print("═" * 42)
    print("1) Añadir tarea")
    print("2) Ver tareas")
    print("3) Completar tarea")
    print("4) Eliminar tarea")
    print("5) Salir")
    print("═" * 42)


def añadir_tarea() -> None:
    """Solicita el nombre de la tarea y la agrega como pendiente.
    Rechaza entradas vacías o de solo espacios.
    """
    tarea = input("📝 Escribí la tarea: ").strip()
    if not tarea:
        print("⚠ La tarea no puede estar vacía.")
        return

    tareas.append({"nombre": tarea, "completada": False})
    print(f"✔ Tarea añadida: “{tarea}”")


def ver_tareas() -> None:
    """Muestra todas las tareas con numeración (base 1) y su estado."""
    if not tareas:
        print("📭 No hay tareas cargadas.")
        return

    print(f"\n📋 Lista de tareas ({len(tareas)}):")
    for i, t in enumerate(tareas, start=1):
        estado = "✅" if t.get("completada") else "❌"
        print(f" {i:>2}. {t.get('nombre', '(sin nombre)')} [{estado}]")


def _indice_valido(indice: int) -> bool:
    """Valida que `indice` (base 0) esté dentro del rango de `tareas`.
    Muestra mensajes claros en caso de error.
    """
    if not tareas:
        print("📭 No hay tareas para operar.")
        return False

    if 0 <= indice < len(tareas):
        return True

    # Mensaje en términos del usuario (base 1)
    print(f"⚠ Número inválido. Elegí un número del 1 al {len(tareas)}.")
    return False


def completar_tarea(indice: int) -> None:
    """Marca como completada la tarea en la posición `indice` (base 0).
    Si ya estaba completada, informa al usuario.
    """
    if _indice_valido(indice):
        if tareas[indice]["completada"]:
            print(f"ℹ La tarea “{tareas[indice]['nombre']}” ya estaba completada.")
            return
        tareas[indice]["completada"] = True
        print(f"✅ Completada: “{tareas[indice]['nombre']}”")


def eliminar_tarea(indice: int) -> None:
    """Elimina la tarea en la posición `indice` (base 0)."""
    if _indice_valido(indice):
        borrada = tareas.pop(indice)
        print(f"🗑 Eliminada: “{borrada.get('nombre', '(sin nombre)')}”")
