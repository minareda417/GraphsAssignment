import heapq

class MSTGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex in self.graph:
            print(f'Vertex {vertex} already exists.')
            return
        self.graph[vertex] = []

    def add_vertices(self, vertices:[str]) -> None:
        for vertex_name in vertices:
            self.add_vertex(vertex_name)

    def add_edge(self, vertex1: str, vertex2:str, weight: int) -> None:
        not_found_vertices = [v for v in [vertex1, vertex2] if v not in self.graph]
        if not_found_vertices:
            print(f'Vertex/vertices {not_found_vertices} is not in graph.')
            return
        if vertex1 == vertex2:
            print(f"MST Graph doesn't have self-loops")
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def add_edges(self, edges:[str, str, int]) -> None:
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    def remove_vertex(self, vertex: str) -> None:
        if vertex not in self.graph:
            print(f"Vertex {vertex} doesn't exist.")
            return
        self.graph.pop(vertex)
        for key in self.graph.keys():
            for edge in self.graph[key]:
                if edge[0] == vertex:
                    self.graph[key].remove(edge)

    def remove_edge(self, vertex1: str, vertex2: str) -> None:
        vertices = [vertex1, vertex2]
        not_found_vertices = [v for v in [vertex1, vertex2] if v not in self.graph]
        if not_found_vertices:
            print(f'Vertex/vertices {not_found_vertices} is not in graph.')
            return
        for vertex in vertices:
            for edge in self.graph[vertex]:
                if edge[0] in vertices:
                    self.graph[vertex].remove(edge)

    def prim(self, root: str):
        if root not in self.graph:
            print(f"{root} not in graph")
            return

        pq = []
        keys = {vertex : float('inf') for vertex in self.graph.keys()}
        parents = {vertex : None for vertex in self.graph.keys()}
        visited = {vertex: False for vertex in self.graph.keys()}
        keys[root] = 0
        heapq.heappush(pq, (0, root))

        mst_weight = 0

        while pq:
            key, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            mst_weight += key

            for vertex, weight in self.graph[u]:
                if  not visited[vertex] and keys[vertex] > weight:
                    parents[vertex] = u
                    keys[vertex] = weight
                    heapq.heappush(pq, (keys[vertex], vertex))

        for vertex in self.graph.keys():
            if parents[vertex] is not None:
                print(f"{parents[vertex]} - {vertex}")

        return mst_weight
