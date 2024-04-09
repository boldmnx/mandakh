class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, movie_title, actor):
        if movie_title not in self.graph:
            self.graph[movie_title] = []
        self.graph[movie_title].append(actor)

newMovie = {
    'title': 'The Matrix',
    'released': 1999
}
newActor = {
    'name': 'Keanu Reeves',
    'age': 18
}

graph = Graph()
graph.add_edge(newMovie['title'], newActor)
graph.add_edge(newMovie['title'], newActor)

print(graph.graph)
