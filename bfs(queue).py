graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'I': ['L'], 'F': [],
    'N': [], 'M': [], 'L': [], 'G': [], 'C': [], 'H': [], 'J': [],
}
visited = []
queue = []


def bfs(visited, graph, snode, enode):
    visited.append(snode)
    queue.append(snode)
    while queue:
        s = queue.pop(0)
        visited.append(s)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
        if s == enode:
            break


startingnode = 'A'
Endingnode = 'C'
bfs(visited, graph, startingnode, Endingnode)
