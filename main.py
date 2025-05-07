from mst import MSTGraph
from directed_graph import DAG
def main():
    dag = DAG()
    graph = MSTGraph()
    while True: 
        print("\nChoose operation:\n1.Topological Sort\n2.Prim Algorithm\n3.Exit")
        try:
            choice = int(input())
            match choice:
                case 1:
                    while True:
                        print("\nChoose operation:\n0.Insert\n1.Add vertex\n2.Add vertices\n3.Add edge"
                            "\n4.Add edges\n5.Delete vertex\n6.Delete edge\n7.In Degree Topological Sort\n8.Exit")
                        try:
                            op = int(input())
                            match op:
                                case 0:
                                    vertices = input("Enter vertex's name: ").split()
                                    dag.insert(vertices)
                                case 1:
                                    vertex = input("Enter vertex's name: ")
                                    dag.add_vertex(vertex)
                                case 2:
                                    vertices = input("Enter vertices names: ").split()
                                    dag.add_vertices(vertices)
                                case 3:
                                    vertex1 = input("Enter first vertex's name: ")
                                    vertex2 = input("Enter Second vertex's name: ")
                                    dag.add_edge(vertex1, vertex2)
                                case 4:
                                    edges = []
                                    while True:
                                        vertex1 = input("Enter first vertex's name: ")
                                        vertex2 = input("Enter Second vertex's name: ")
                                        edge = (vertex1, vertex2)
                                        edges.append(edge)
                                        cont = input("Do you want to add another edge? [y/n]: ")
                                        while cont.lower() not in ['y', 'n']:
                                            cont = input("Do you want to add another edge? [y/n]: ")
                                        if cont.lower() == 'n':
                                            dag.add_edges(edges)
                                            break
                                case 5:
                                    vertex = input("Enter vertex's name: ")
                                    dag.remove_vertex(vertex)
                                case 6:
                                    vertex1 = input("Enter first vertex's name: ")
                                    vertex2 = input("Enter Second vertex's name: ")
                                    dag.remove_edge(vertex1, vertex2)
                                case 7:
                                    print(f"Applying In-Degree Topological Sort...")
                                    dag.degree_topological_sort()
                                case 8:
                                    print("Thank you")
                                    break
                                case _:
                                    print("Invalid option. Please choose a number between 1 and 8.")
                        except ValueError:
                            print("Please enter a valid number.")
                    pass
                case 2:
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
                case 3:
                    break
        except ValueError:
            print("Please enter a valid number.")
if __name__== "__main__":
    main()