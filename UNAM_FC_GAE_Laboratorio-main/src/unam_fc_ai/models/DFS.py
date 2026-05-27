""""
===========================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahí Mendez Rincon
Ayduante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Giovanni Alejandri Espinosa
Año escolar: 2026-2
Copyright (c) 2025 UNAM - MIT License
Version: 1.0
This software is for educational purposes.
The accuracy of the models depends strictly on the quality
and preocessing of the input data.
-----------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI develped at UNAM.
============================================================================
"""

from collections import deque

def dfs(grafo, nodo_inicial):
    """
    Implementación iterativa de DFS para evitar problemas de profundidad de recursión.
    Optimización: Cambiada de recursiva a iterativa usando una pila (deque) para manejar
    grafos profundos sin riesgo de stack overflow.
    """
    visitados = set()
    pila = [nodo_inicial]  # Usamos una pila para simular la recursión
    orden_visita = []  # Lista para almacenar el orden de visita

    while pila:
        nodo = pila.pop()  # Sacamos el último elemento (LIFO)
        if nodo not in visitados:
            visitados.add(nodo)
            orden_visita.append(nodo)  # Agregamos al orden de visita
            # Agregamos los vecinos en orden inverso para mantener el orden DFS
            # Optimización: Invertimos la lista de vecinos para que el primer vecino
            # sea procesado último, manteniendo el comportamiento DFS original.
            for vecino in reversed(grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(vecino)

    return orden_visita  # Retornamos el orden en lugar de imprimir

def dfs_recursiva(grafo, nodo, visitados=None):
    """
    Versión recursiva, no se borra para que se comparen los resultados.
    Puede causar stack overflow en grafos muy profundos.
    """
    if visitados is None:
        visitados = set()

    visitados.add(nodo)
    print(nodo, end=" ")

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_recursiva(grafo, vecino, visitados)

# Grafo de ejemplo
grafo_ejemplo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("Orden de exploración DFS iterativa empezando desde 2:")
orden = dfs(grafo_ejemplo, 2)
print(" ".join(map(str, orden)))

print("\nVersión recursiva original:")
dfs_recursiva(grafo_ejemplo, 2)