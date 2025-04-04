import random

def experimento_figus(n_repeticiones, figus_total):
    total_figus_compradas = []
    for _ in range(n_repeticiones):
        figus_compradas = cuantas_figus(figus_total=figus_total)
        total_figus_compradas.append(figus_compradas)
    return sum(total_figus_compradas) / len(total_figus_compradas)

def cuantas_figus(figus_total):
    counter = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] += 1
        counter += 1
    return counter

def crear_album(figus_total):
    return [0] * figus_total

def album_incompleto(album):
    return sum([i>0 for i in album]) < len(album)

def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)

if __name__== "__main__":
    print(experimento_figus(n_repeticiones=100, figus_total=860))