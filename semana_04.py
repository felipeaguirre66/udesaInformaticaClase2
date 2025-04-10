import csv

# Global: nombre del archivo CSV
NOMBRE_ARCHIVO = 'arbolado-en-espacios-verdes.csv'

# --- Funciones ejercicios 1-4 ---
# 1
import csv

def arboles_parque(nombre_archivo, nombre_parque):
    all_trees = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila['espacio_ve'] == nombre_parque:
                id_arbol = fila['id_arbol']
                fila_sin_id = {k: v for k, v in fila.items() if k != 'id_arbol'}
                all_trees.append({id_arbol: fila_sin_id})
    return all_trees

# 2
def arbol_mas_popular(nombre_parque):
    trees = arboles_parque(NOMBRE_ARCHIVO, nombre_parque)
    counts = {}
    for t in trees:
        for datos in t.values():
            nombre_com = datos.get('nombre_com')
            counts[nombre_com] = counts.get(nombre_com, 0) + 1
    mas_popular = max(counts, key=counts.get)
    return mas_popular

# 3
def n_mas_altos(nombre_parque, n):
    trees = arboles_parque(NOMBRE_ARCHIVO, nombre_parque)
    trees_list = []
    for t in trees:
        for id_arbol, tree_data in t.items():
            try:
                altura = float(tree_data.get('altura_tot', 0))
            except:
                altura = 0
            trees_list.append((id_arbol, tree_data, altura))
    trees_sorted = sorted(trees_list, key=lambda x: x[2], reverse=True)
    top_n = trees_sorted[:n]
    resultado = []
    for _, tree_data, _ in top_n:
        resultado.append(tree_data['nombre_com'])
    return resultado

# 4
def altura_promedio(nombre_parque, especie):
    especie = str(especie)
    trees = arboles_parque(NOMBRE_ARCHIVO, nombre_parque)
    suma_alturas = 0.0
    count = 0
    for t in trees:
        for tree_data in t.values():
            if tree_data.get('id_especie') == especie:
                try:
                    altura = float(tree_data.get('altura_tot', 0))
                    suma_alturas += altura
                    count += 1
                except:
                    continue
    return suma_alturas / count if count > 0 else None

# --- Funciones extra ---

def parques_mas_arboles(nombre_archivo, n):
    counts = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            parque = fila.get('espacio_ve')
            if parque:
                counts[parque] = counts.get(parque, 0) + 1
    if not counts:
        return None
    sorted_parques = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_parques[:n]

def parques_altura_promedio(nombre_archivo, n):
    alturas = {}
    counts = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            parque = fila.get('espacio_ve')
            try:
                altura = float(fila.get('altura_tot', 0))
            except:
                altura = 0
            if parque:
                alturas[parque] = alturas.get(parque, 0) + altura
                counts[parque] = counts.get(parque, 0) + 1
    promedios = {parque: alturas[parque] / counts[parque] for parque in alturas if counts[parque] > 0}
    if not promedios:
        return None
    sorted_parques = sorted(promedios.items(), key=lambda item: item[1], reverse=True)
    return sorted_parques[:n]

def parques_variedad_especies(nombre_archivo, n):
    park_species = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            parque = fila.get('espacio_ve')
            especie = fila.get('id_especie')
            if parque and especie:
                if parque not in park_species:
                    park_species[parque] = set()
                park_species[parque].add(especie)
    counts = {parque: len(especies) for parque, especies in park_species.items()}
    if not counts:
        return None
    sorted_parques = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_parques[:n]


def especie_mas_ejemplares(nombre_archivo):
    counts = {}
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            especie = fila.get('nombre_com')
            if especie:
                counts[especie] = counts.get(especie, 0) + 1
    if not counts:
        return None
    max_count = max(counts.values())
    especies_max = [esp for esp, count in counts.items() if count == max_count]
    return especies_max, max_count

def razon_especies_exoticas_autoctonas(nombre_archivo):
    count_exoticas = 0
    count_autotctonas = 0
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            origen = fila.get('origen', '').strip().lower()
            if origen == 'nativo/autóctono':
                count_autotctonas += 1
            else:
                count_exoticas += 1
    if count_autotctonas == 0:
        return None
    ratio = count_exoticas / count_autotctonas
    return ratio

if __name__ == '__main__':

    # --- Informe ---
    sorted_parques = parques_mas_arboles(NOMBRE_ARCHIVO, 2)
    print(f"Parques con mas arboles: {sorted_parques}")

    sorted_parques = parques_altura_promedio(NOMBRE_ARCHIVO, 2)
    print(f"Parques con mayor altura promedio de sus arboles: {sorted_parques}")

    sorted_parques = parques_variedad_especies(NOMBRE_ARCHIVO, 2)
    print(f"Parques con mayor variedad de especies: {sorted_parques}")

    especies_max, ejemplares = especie_mas_ejemplares(NOMBRE_ARCHIVO)
    print(f"La especie con mas ejemplares en la ciudad: {especies_max} (Cantidad: {ejemplares})")

    razon = razon_especies_exoticas_autoctonas(NOMBRE_ARCHIVO)
    if razon is not None:
        print(f"La razon entre especies exóticas y autóctonas es: {razon:.2f}")
    else:
        print("No se pudo calcular la razon (división por cero).")