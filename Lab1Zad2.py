from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    Oblicza najkrótszą ścieżkę w grafie nieważonym za pomocą BFS.
    
    :param graph: Graf jako słownik {wierzchołek: [lista sąsiednich wierzchołków]}.
    :param start: Wierzchołek początkowy (str).
    :param end: Wierzchołek końcowy (str).
    :return: Najkrótsza ścieżka jako lista wierzchołków (list[str]) lub [] jeśli brak ścieżki.
    """
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)
            queue.extend(path + [neighbor] for neighbor in graph.get(node, []) if neighbor not in visited)

    return []


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    start = "A"
    end = "F"

    shortest_path = bfs_shortest_path(graph, start, end)

    print(f"Najkrótsza ścieżka z {start} do {end}: {shortest_path}")


if __name__ == "__main__":
    main()
