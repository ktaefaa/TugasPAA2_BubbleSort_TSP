import itertools

def tsp(graph, start):
    # Membangkitkan semua permutasi dari titik-titik yang dikunjungi
    vertices = list(graph.keys())
    vertices.remove(start)
    perm = list(itertools.permutations(vertices))

    # Menyimpan jalur terpendek dan panjangnya
    shortest_path = None
    shortest_distance = float('inf')

    # Memeriksa setiap permutasi
    for p in perm:
        path = [start] + list(p) + [start]
        distance = 0
        # Menghitung panjang jalur
        for i in range(len(path) - 1):
            distance += graph[path[i]][path[i + 1]]
        # Memperbarui jalur terpendek jika ditemukan jalur yang lebih pendek
        if distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
    return shortest_path, shortest_distance


# Contoh penggunaan
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}
start_vertex = 'A'
shortest_path, shortest_distance = tsp(graph, start_vertex)
print("Jalur terpendek:", shortest_path)
print("Panjang jalur terpendek:", shortest_distance)