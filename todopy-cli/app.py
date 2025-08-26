"""
app.py — Gestor de Tareas por Consola

Descripción
-----------
Orquesta el menú interactivo y delega la lógica en `funciones.py`.
Carga las tareas al iniciar y guarda los cambios tras añadir, completar o eliminar.

Uso
---
    python app.py

Entradas del usuario
--------------------
- Menú: números del 1 al 5.
- Completar/Eliminar: número de tarea (mostrado en la lista).

Convenciones UX
---------------
- Al usuario se le muestran índices desde 1, pero internamente se convierten a base 0.
- Se informa el resultado de cada acción y se confirma el guardado (💾).
- `funciones.py` maneja la persistencia en `tareas.json`.

Notas
-----
- Este script no valida entradas no numéricas en "Completar/Eliminar".
  Si querés robustecerlo sin cambiar el flujo, podés crear un helper `pedir_entero()`
  y usarlo en lugar de `int(opc)`. (Lo dejamos fuera para respetar tu lógica actual.)
"""

import funciones as fn
import os 
import time

# Cargar tareas guardadas (si existen)
fn.cargar_tareas()
os.system("cls")

# Bucle principal del menú
while True:
    os.system("cls")
    print("\n" + "=" * 50)
    fn.mostrar_menu()
    opcion = input("Seleccioná una opción (1–5): ").strip()

    if opcion == "1":
        # Añadir una nueva tarea (el input se pide dentro de la función)
        print("\n🟢 Añadir tarea")
        print("Escribí el nombre de la tarea cuando se te solicite.\n")
        fn.añadir_tarea()
        fn.guardar_tareas()
        print("💾 Cambios guardados.\n")

    elif opcion == "2":
        # Mostrar listado completo de tareas con estado
        print("\n📋 Tus tareas")
        fn.ver_tareas()
        print("— Fin de la lista —\n")
        input("📝 Escribir ¨1¨ para volver al menú ")

    elif opcion == "3":
        # Marcar una tarea como completada (índice mostrado al usuario inicia en 1)
        print("\n✅ Completar tarea")
        print("Elegí el número de la tarea a marcar como completada.")
        print("\nLista de tareas:")
        fn.ver_tareas()
        opc = input("➡️ Número a completar: ")
        fn.completar_tarea(int(opc) - 1)
        fn.guardar_tareas()
        print("💾 Cambios guardados.\n")

    elif opcion == "4":
        # Eliminar una tarea por número (índice mostrado al usuario inicia en 1)
        print("\n🗑️ Eliminar tarea")
        print("Elegí el número de la tarea a eliminar.")
        print("\nLista de tareas:")
        fn.ver_tareas()
        opc = input("➡️ Número a eliminar: ")
        fn.eliminar_tarea(int(opc) - 1)
        fn.guardar_tareas()
        print("💾 Cambios guardados.\n")

    elif opcion == "5":
        # Salida ordenada del programa (se guarda por las dudas)
        print("\n👋 Guardando y saliendo... ¡Hasta luego!\n")
        fn.guardar_tareas()
        time.sleep(2) # Pausa de 2 segundos

        break

    else:
        # Entrada inválida en el menú
        print("\n⚠️ Opción no válida. Elegí un número del 1 al 5.\n")
        time.sleep(2) # Pausa de 2 segundos
