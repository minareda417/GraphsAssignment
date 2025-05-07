import heapq

class MSTGraph:
    def __init__(self):
        self.graph = {}
        self.vertices_count = 0

    def add_vertex(self, vertex: str) -> None:
        if vertex in self.graph:
            print(f'Vertex {vertex} already exists.')
            return
        self.graph[vertex] = []
        self.vertices_count += 1

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
        self.vertices_count -= 1

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
                if  visited[u] and keys[vertex] > weight:
                    parents[vertex] = u
                    keys[vertex] = weight
                    heapq.heappush(pq, (keys[vertex], vertex))

        for vertex in self.graph.keys():
            if parents[vertex] is not None:
                print(f"{parents[vertex]} - {vertex}")

        return mst_weight


def main():
    print("Prim Algorithm")
    graph = MSTGraph()
    while True:
        print("\nChoose operation:\n1.Add vertex\n2.Add vertices\n3.Add edge"
              "\n4.Add edges\n5.Delete vertex\n6.Delete edge\n7.Prim\n8.Exit")
        try:
            op = int(input())
            match op:
                case 1:
                    vertex = input("Enter vertex's name: ")
                    graph.add_vertex(vertex)
                case 2:
                    vertices = input("Enter vertices names: ").split()
                    graph.add_vertices(vertices)
                case 3:
                    vertex1 = input("Enter first vertex's name: ")
                    vertex2 = input("Enter Second vertex's name: ")
                    weight = int(input("Enter edge's weight: "))
                    graph.add_edge(vertex1, vertex2, weight)
                case 4:
                    edges = []
                    while True:
                        vertex1 = input("Enter first vertex's name: ")
                        vertex2 = input("Enter Second vertex's name: ")
                        weight = int(input("Enter edge's weight: "))
                        edge = (vertex1, vertex2, weight)
                        edges.append(edge)
                        cont = input("Do you want to add another edge? [y/n]: ")
                        while cont.lower() not in ['y', 'n']:
                            cont = input("Do you want to add another edge? [y/n]: ")
                        if cont.lower() == 'n':
                            graph.add_edges(edges)
                            break
                case 5:
                    vertex = input("Enter vertex's name: ")
                    graph.remove_vertex(vertex)
                case 6:
                    vertex1 = input("Enter first vertex's name: ")
                    vertex2 = input("Enter Second vertex's name: ")
                    graph.remove_edge(vertex1, vertex2)
                case 7:
                    root = input("Enter root's name: ")
                    print(f"MST weight = {graph.prim(root)}")
                case 8:
                    print("Thank you")
                    break
                case _:
                    print("Invalid option. Please choose a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")



if __name__== "__main__":
    main()