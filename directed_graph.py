class DAG:   
    def __init__(self):
        self.graph = {}
    def insert(self, vertices: list[str]) -> None:
        # split the vertices by space and remove duplicates
        for vertex in vertices:
            if self.graph.get(vertex) is not None:
                print(f'Vertex {vertex} already exists.')
                return
            if self.graph == {}:
                self.add_vertex(vertex)
            else:
                # Draw an edge from the last vertex to the new vertex
                last_vertex = list(self.graph.keys())[-1]
                self.add_vertex(vertex)
                self.add_edge(last_vertex, vertex)

    def add_vertex(self, vertex: str) -> None:
        if vertex in self.graph:
            print(f'Vertex {vertex} already exists.')
            return
        self.graph[vertex] = []

    def add_vertices(self, vertices: list[str]) -> None:
        for vertex_name in vertices:
            self.add_vertex(vertex_name)

    def add_edge(self, from_vertex: str, to_vertex:str) -> None:
        not_found_vertices = [v for v in [from_vertex, to_vertex] if v not in self.graph]
        if not_found_vertices:
            print(f'Vertex/vertices {not_found_vertices} is not in graph.')
            return
        if from_vertex == to_vertex:
            print(f"DAG Graph doesn't have self-loops")
            return
        #  If the edge causes a cycle, do not add it
        if self.is_a_cycle(to_vertex, from_vertex):
            print(f"Adding edge from {from_vertex} to {to_vertex} would create a cycle.")
            return
        self.graph[from_vertex].append(to_vertex)
        
    def is_a_cycle(self, key: str, end: str) -> bool:
        visited = set()
        #  Check for cycles using DFS
        def dfs(key: str) -> bool:
            if key == end:
                return True
            visited.add(key)
            for neighbor in self.graph.get(key, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(key)


    def add_edges(self, edges: list[tuple[str, str]]) -> None:
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def remove_vertex(self, vertex: str) -> None:
        if vertex not in self.graph:
            print(f"Vertex {vertex} doesn't exist.")
            return
        self.graph.pop(vertex)
        for key in self.graph:
            if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)

    def remove_edge(self, from_vertex: str, to_vertex: str) -> None:
        not_found_vertices = [v for v in [from_vertex, to_vertex] if v not in self.graph]
        if not_found_vertices:
            print(f'Vertex/vertices {not_found_vertices} is not in graph.')
            return
        self.graph[from_vertex].remove(to_vertex)

    
    def degree_topological_sort(self) -> None:
        # Initialize the degree of all vertices to 0
        in_degree = {vertex : 0 for vertex in self.graph}
        for vertex in self.graph:
            # Increment the degree of each vertex by its neighbors if found
            for neighbor in self.graph[vertex]:
                in_degree[neighbor] += 1
                print(f"Degree of {neighbor}: {in_degree[neighbor]}")
        # Initialize a queue with all vertices of degree 0
        queue = [v for v in in_degree if in_degree[v] == 0]
        print(f"Queue: {queue}")
        topological_order = []
        while queue:
            print(f"Queue: {queue}")
            vertex = queue.pop(0)
            # Print degree of 
            print(f"Degree of {vertex}: {in_degree[vertex]}")
            # Append vertices of degree 0 to the topological order
            topological_order.append(vertex)
            for neighbor in self.graph[vertex]:
                # Decrement the degree of each neighbor by 1
                print(f"Degree of {neighbor}: {in_degree[neighbor]}")
                in_degree[neighbor] -= 1
                # Add neighbor to the queue is its degree becomes 0
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            # Print the topological order
        print(f"Topological order: {topological_order}")
