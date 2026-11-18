def _mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def mezcla_equilibrada(lista):
    """Simulación de mezcla equilibrada detectando bloques ordenados naturalmente."""
    if not lista:
        return []

    # Paso 1: Dividir la lista en bloques ordenados naturales (runs)
    runs = []
    run_actual = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            run_actual.append(lista[i])
        else:
            runs.append(run_actual)
            run_actual = [lista[i]]
    runs.append(run_actual)

    # Paso 2: Intercalar los runs de manera equilibrada hasta tener uno solo
    while len(runs) > 1:
        nuevos_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                nuevos_runs.append(_mezclar(runs[i], runs[i + 1]))
            else:
                nuevos_runs.append(runs[i])
        runs = nuevos_runs

    return runs[0]


# Ejemplo de uso:
if __name__ == "__main__":
    datos = [2, 5, 9, 1, 3, 8, 4, 6]
    print("Lista original:", datos)
    print("Lista ordenada por Mezcla Equilibrada:", mezcla_equilibrada(datos))