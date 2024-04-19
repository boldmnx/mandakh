class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.data] = node

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, source, target, edge_type=None, role=None):
        self.type = edge_type
        self.source = source
        self.target = target
        self.role = role if role else []

    def __str__(self):
        return f"Edge: {self.source.data} --{self.type}-> {self.target.data}"


class Node:
    def __init__(self, data, label=None):
        self.data = data
        self.label = label

    def __str__(self):
        return f"Node: {self.data}"


class Movie:
    def __init__(self, title, tagline=None, released=None):
        self.title = title
        self.tagline = tagline
        self.released = released

    def __str__(self):
        return f"{self.title} (Movie)"


class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (Person)"


if __name__ == "__main__":

    graph = Graph()

    # movies
    inception = Node(
        Movie("Inception", "Your mind is the scene of the crime", 2010), label="Movie")
    shawshank = Node(Movie("The Shawshank Redemption", 1994), label="Movie")
    # actors
    leonardo = Node(Person("Leonardo DiCaprio"), label="Person")
    nolan = Node(Person("Christopher Nolan"), label="Person")
    tim = Node(Person("Tim Robbins"), label="Person")
    frank = Node(Person("Frank Darabont"), label="Person")
    #add movie
    graph.add_node(inception)
    graph.add_node(shawshank)
    #add actor
    graph.add_node(leonardo)
    graph.add_node(nolan)
    graph.add_node(tim)
    graph.add_node(frank)
    #edges
    edge1 = Edge(tim, shawshank, edge_type="Actor")
    edge2 = Edge(frank, shawshank, edge_type="Director")
    edge3 = Edge(leonardo, inception, edge_type="Actor")
    edge4 = Edge(nolan, inception, edge_type="Director")

    graph.add_edge(edge1)
    graph.add_edge(edge2)
    graph.add_edge(edge3)
    graph.add_edge(edge4)

    print("Graph Nodes:")
    for node in graph.nodes.values():
        print(node)

    print("\nGraph Edges:")
    for edge in graph.edges:
        print(edge)
